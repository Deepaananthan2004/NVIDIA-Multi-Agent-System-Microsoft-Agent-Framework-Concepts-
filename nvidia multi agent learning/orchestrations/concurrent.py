import asyncio
from typing import List
from core.agent import NIMAgent


class ConcurrentOrchestrator:

    def __init__(self, participants: List[NIMAgent], synthesizer: NIMAgent = None):
        self.participants = participants
        self.synthesizer = synthesizer

    async def run_agent(self, agent: NIMAgent, prompt: str):

        try:
            print(f"⚡ {agent.name} working...\n")

            response = await agent.run(prompt)

            return {
                "agent": agent.name,
                "response": response,
                "status": "success"
            }

        except Exception as e:

            return {
                "agent": agent.name,
                "response": str(e),
                "status": "error"
            }

    async def run(self, prompt: str):

        print("\n🚀 Concurrent Multi-Agent System\n")
        print(f"Task: {prompt}\n")

        # run agents in parallel
        tasks = [self.run_agent(agent, prompt) for agent in self.participants]

        results = await asyncio.gather(*tasks)

        print("\n📊 Agent Results\n")

        for r in results:
            print(f"{r['agent']}:\n{r['response'][:300]}\n")

        # optional synthesis step
        if self.synthesizer:

            print("\n🧠 Synthesizing Final Answer...\n")

            combined = "\n\n".join(
                [f"{r['agent']}:\n{r['response']}" for r in results if r["status"] == "success"]
            )

            final_prompt = f"""
User Task:
{prompt}

Expert Responses:
{combined}

Combine the expert insights and produce a clear final answer.
"""

            final_answer = await self.synthesizer.run(final_prompt)

            print("✅ Final Synthesized Answer:\n")
            print(final_answer)

            return {
                "task": prompt,
                "results": results,
                "final": final_answer
            }

        return {
            "task": prompt,
            "results": results
        }