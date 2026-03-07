import asyncio,sys
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.agent import NIMAgent


async def main():
    print("🤖 NVIDIA Agent Chat\n")
    print("Type 'exit' to quit.\n")

    agent = NIMAgent(
        name="HelperBot",
        instructions="You are a helpful AI assistant. Always give clear answers."
    )

    while True:
        user_prompt = input("You: ")

        if user_prompt.lower() in ["exit", "quit"]:
            print("\n👋 Ending chat...")
            break

        try:
            response = await agent.run(user_prompt)
            print("\nAgent:", response, "\n")

        except Exception as e:
            print("⚠️ Error:", e)


if __name__ == "__main__":
    asyncio.run(main())