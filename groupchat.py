import asyncio,sys
sys.path.append('..')
from core.agent import NIMAgent
from orchestrations.concurrent import ConcurrentOrchestrator

async def main():
    a=NIMAgent("Researcher","Give research.")
    b=NIMAgent("Marketer","Give marketing.")
    c=NIMAgent("Legal","Give legal view.")

    orch=ConcurrentOrchestrator([a,b,c])
    await orch.run("Launching electric bike")

asyncio.run(main())