import asyncio,sys
sys.path.append('..')
from core.agent import NIMAgent

async def main():
    agent=NIMAgent("HelperBot","You are helpful.")
    r=await agent.run("Explain Microsoft Agent Framework")
    print(r)

asyncio.run(main())