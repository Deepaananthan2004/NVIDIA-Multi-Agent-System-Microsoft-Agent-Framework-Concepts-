from typing import Dict, List, Any

class MemoryProvider:
    def __init__(self):
        self.facts: Dict[str, Any] = {}
        self.session_memories: Dict[str, Dict[str, Any]] = {}

    def store_fact(self, key: str, value: Any, session_id: str = None):
        if session_id:
            if session_id not in self.session_memories:
                self.session_memories[session_id] = {}
            self.session_memories[session_id][key] = value
        else:
            self.facts[key] = value

    def get_fact(self, key: str, session_id: str = None):
        if session_id and session_id in self.session_memories:
            return self.session_memories[session_id].get(key)
        return self.facts.get(key)

    def get_all_facts(self, session_id: str = None):
        if session_id and session_id in self.session_memories:
            return self.session_memories[session_id]
        return self.facts

    def inject_into_messages(self, messages: List[Dict], session_id: str = None):
        facts = self.get_all_facts(session_id)
        if facts:
            facts_text = "\n".join(f"- {k}: {v}" for k, v in facts.items())
            system_message = {
                "role": "system",
                "content": f"Remember these user facts:\n{facts_text}"
            }
            if messages and messages[0].get("role") == "system":
                messages[0]["content"] += f"\n\n{system_message['content']}"
            else:
                messages.insert(0, system_message)
        return messages