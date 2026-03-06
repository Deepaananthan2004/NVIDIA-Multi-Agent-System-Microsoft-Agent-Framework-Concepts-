import asyncio,subprocess,sys

DEMOS=[
"demos/01_basic_agent.py",
"demos/02_session_memory.py",
"demos/03_groupchat.py",
"demos/04_concurrent.py"
]

async def main():
    for d in DEMOS:
        subprocess.run([sys.executable,d])
        input("Next demo...")

asyncio.run(main())