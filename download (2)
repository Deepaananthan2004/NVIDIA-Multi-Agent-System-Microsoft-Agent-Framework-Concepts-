from typing import List
from ..core.agent import NIMAgent

class GroupChatOrchestrator:

    def __init__(self, participants: List[NIMAgent], max_rounds: int = 5):
        self.participants = {a.name: a for a in participants}
        self.max_rounds = max_rounds
        self.history = []
        self.round = 0

    async def run(self, task):
        print(f"Task: {task}")
        self.history.append({"role":"user","content":task})

        names=list(self.participants.keys())

        while self.round < self.max_rounds:
            speaker = self.participants[names[self.round % len(names)]]
            context = task + "\nConversation:\n"

            for m in self.history:
                context += m["content"] + "\n"

            resp = await speaker.run(context)

            print(f"{speaker.name}: {resp[:200]}")
            self.history.append({"role":"assistant","content":resp})
            self.round+=1

        return self.history