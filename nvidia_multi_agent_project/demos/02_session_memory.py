import asyncio,sys
sys.path.append('..')
from core.agent import NIMAgent
from core.memory import MemoryProvider

async def main():
    mem=MemoryProvider()
    agent=NIMAgent("MemoryBot","Remember user facts.",memory=mem)

    await agent.run("My name is Alex")
    mem.store_fact("name","Alex",agent.session.session_id)

    r=await agent.run("What is my name?")
    print(r)

asyncio.run(main())