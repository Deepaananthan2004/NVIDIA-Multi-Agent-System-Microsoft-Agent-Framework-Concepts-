import asyncio
import sys
import os
import re

# add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.agent import NIMAgent
from core.memory import MemoryProvider


# ----------------------------
# Automatic Fact Extraction
# ----------------------------
def extract_user_facts(text, memory, session_id):

    text_lower = text.lower()

    patterns = {
        "name": r"my name is ([a-zA-Z ]+)",
        "age": r"i am (\d{1,3}) years old",
        "location": r"i live in ([a-zA-Z ]+)",
        "education": r"i study ([a-zA-Z &]+)",
        "education_alt": r"i am studying ([a-zA-Z &]+)",
        "job": r"i work as ([a-zA-Z ]+)",
        "hobby": r"my hobby is ([a-zA-Z ]+)",
        "skills": r"my skills are ([a-zA-Z ,]+)",
        "dob": r"my date of birth is ([0-9\-\/ ]+)"
    }

    for key, pattern in patterns.items():

        match = re.search(pattern, text_lower)

        if match:

            value = match.group(1).strip().title()

            if key == "education_alt":
                key = "education"

            memory.store_fact(key, value, session_id)

            print(f"🧠 Stored memory → {key}: {value}")


# ----------------------------
# Display Stored Memory
# ----------------------------
def show_memory(memory, session_id):

    facts = memory.get_all_facts(session_id)

    if not facts:
        return

    print("\n📚 Agent Memory")
    print("-----------------")

    for k, v in facts.items():
        print(f"{k.capitalize()}: {v}")

    print()


# ----------------------------
# Chat System
# ----------------------------
async def main():

    print("\n🤖 Intelligent Memory Agent")
    print("The agent automatically learns facts from conversation.\n")

    print("Commands:")
    print(" • memory → show stored memory")
    print(" • exit → quit\n")

    mem = MemoryProvider()

    agent = NIMAgent(
        name="MemoryBot",
        instructions=(
            "You are a helpful assistant that remembers user facts "
            "like name, age, education, location, hobbies, and skills. "
            "Use stored information when answering questions."
        ),
        memory=mem
    )

    while True:

        user_prompt = input("You: ")

        if user_prompt.lower() == "exit":
            print("\n👋 Chat ended.")
            break

        if user_prompt.lower() == "memory":
            show_memory(mem, agent.session.session_id)
            continue

        # auto-detect facts
        extract_user_facts(user_prompt, mem, agent.session.session_id)

        try:

            response = await agent.run(user_prompt)

            print("\nAgent:", response, "\n")

        except Exception as e:

            print("⚠️ Error:", e)


# ----------------------------
# Run Program
# ----------------------------
if __name__ == "__main__":
    asyncio.run(main())