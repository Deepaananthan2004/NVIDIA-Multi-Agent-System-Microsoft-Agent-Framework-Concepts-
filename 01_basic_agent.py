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
        self.session.add_message("user", prompt)

        messages = [{"role": "system", "content": self.instructions}]
        messages.extend(self.session.get_messages())
        messages = self.memory.inject_into_messages(messages, self.session.session_id)

        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=messages,
            temperature=0.7,
            max_tokens=1024
        )

        text = response.choices[0].message.content
        self.session.add_message("assistant", text)
        return text