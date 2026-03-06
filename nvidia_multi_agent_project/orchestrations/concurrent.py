import asyncio
from typing import List
from ..core.agent import NIMAgent

class ConcurrentOrchestrator:

    def __init__(self, participants: List[NIMAgent]):
        self.participants = participants

    async def run_agent(self, agent, prompt):
        resp = await agent.run(prompt)
        return {"agent":agent.name,"response":resp}

    async def run(self, prompt):
        tasks=[self.run_agent(a,prompt) for a in self.participants]
        results = await asyncio.gather(*tasks)

        for r in results:
            print(r["agent"],":",r["response"][:200])

        return results