import asyncio
from core.agent import NIMAgent
from orchestrations.concurrent import ConcurrentOrchestrator


async def main():

    researcher = NIMAgent(
        "ResearchAgent",
        "Provide factual market insights and trends."
    )

    marketer = NIMAgent(
        "MarketingAgent",
        "Create strong marketing ideas and positioning."
    )

    technical = NIMAgent(
        "TechAgent",
        "Analyze technical feasibility and features."
    )

    risk = NIMAgent(
        "RiskAgent",
        "Identify risks and challenges."
    )

    synthesizer = NIMAgent(
        "FinalSynthesizer",
        "Combine expert insights into a final recommendation."
    )

    orchestrator = ConcurrentOrchestrator(
        participants=[researcher, marketer, technical, risk],
        synthesizer=synthesizer
    )

    task = input("Enter business idea: ")

    await orchestrator.run(task)


asyncio.run(main())