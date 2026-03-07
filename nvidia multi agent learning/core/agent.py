import os
from openai import OpenAI
from dotenv import load_dotenv
from .session import AgentSession
from .memory import MemoryProvider

load_dotenv()

class NIMAgent:

    def __init__(self, name, instructions, model_id=None, session=None, memory=None):
        self.name = name
        self.instructions = instructions
        self.model_id = model_id or os.getenv("MODEL_ID")
        self.session = session or AgentSession()
        self.memory = memory or MemoryProvider()

        self.client = OpenAI(
            base_url=os.getenv("NVIDIA_BASE_URL"),
            api_key=os.getenv("NVIDIA_API_KEY")
        )

    async def run(self, prompt):

        # store user message
        self.session.add_message("user", prompt)

        messages = [{"role": "system", "content": self.instructions}]
        messages.extend(self.session.get_messages())

        # inject memory
        messages = self.memory.inject_into_messages(messages, self.session.session_id)

        try:
            response = self.client.chat.completions.create(
                model=self.model_id,
                messages=messages,
                temperature=0.7,
                max_tokens=1024
            )

            # extract response safely
            text = ""

            if response and response.choices:
                msg = response.choices[0].message

                if msg.content:
                    text = msg.content
                else:
                    text = str(msg)

            if not text:
                text = "No response generated."

            # store response
            self.session.add_message("assistant", text)

            return text

        except Exception as e:
            print("API Error:", e)
            return "Error generating response."