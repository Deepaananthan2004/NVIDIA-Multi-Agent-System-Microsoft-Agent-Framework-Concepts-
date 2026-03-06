import asyncio,sys
sys.path.append('..')
from core.agent import NIMAgent
from orchestrations.groupchat import GroupChatOrchestrator

async def main():
    writer=NIMAgent("Writer","Create slogans.")
    reviewer=NIMAgent("Reviewer","Review slogans.")

    orch=GroupChatOrchestrator([writer,reviewer])

    await orch.run("Create slogan for eco bike")

asyncio.run(main())