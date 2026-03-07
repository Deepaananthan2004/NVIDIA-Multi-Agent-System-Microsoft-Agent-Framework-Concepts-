import asyncio
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.agent import NIMAgent
from orchestrations.groupchat import GroupChatOrchestrator


async def main():

    print("\n🤖 Multi-Agent AI System (Planner → Worker → Critic → Finalizer)\n")
    print("Type 'exit' or 'q' to stop.\n")

    # Planner Agent
    planner = NIMAgent(
        name="PlannerAgent",
        instructions=(
            "You are a strategic planner. Break the user request into a clear task plan "
            "that other agents can follow."
        )
    )

    # Worker Agent
    worker = NIMAgent(
        name="WorkerAgent",
        instructions=(
            "You are a creative AI worker. Execute the task plan and generate the main content."
        )
    )

    # Critic Agent
    critic = NIMAgent(
        name="CriticAgent",
        instructions=(
            "You are a critic. Analyze the worker output and suggest improvements."
        )
    )

    # Finalizer Agent
    finalizer = NIMAgent(
        name="FinalAgent",
        instructions=(
            "You produce the final polished answer by combining the worker output "
            "and critic feedback."
        )
    )
    # Group chat orchestrator
    orchestrator = GroupChatOrchestrator(
        participants=[planner, worker, critic, finalizer],
        max_rounds=6
    )

    while True:

        task = input("Enter task: ")

        if task.lower() in ["exit", "q"]:
            print("\n👋 Ending Multi-Agent Session.")
            break

        print("\n📌 Planner Agent Thinking...\n")
        plan = await planner.run(task)

        print("Planner Output:\n", plan, "\n")

        print("⚙️ Worker Agent Executing...\n")
        work = await worker.run(f"Plan:\n{plan}\n\nExecute the task.")

        print("Worker Output:\n", work, "\n")

        print("🔍 Critic Agent Reviewing...\n")
        review = await critic.run(f"Review this output and suggest improvements:\n{work}")

        print("Critic Feedback:\n", review, "\n")

        print("✨ Finalizer Agent Producing Final Result...\n")
        final = await finalizer.run(
            f"Original task: {task}\n\nWorker Output:\n{work}\n\nCritic Feedback:\n{review}\n\nProduce final improved result."
        )

        print("✅ Final Result:\n", final, "\n")



    await orchestrator.run(task)


if __name__ == "__main__":
    asyncio.run(main())