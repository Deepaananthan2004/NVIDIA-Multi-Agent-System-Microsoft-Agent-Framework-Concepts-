import uuid
from datetime import datetime
from typing import List, Dict, Any

class AgentSession:
    def __init__(self, session_id: str = None):
        self.session_id = session_id or str(uuid.uuid4())
        self.created_at = datetime.now()
        self.messages: List[Dict[str, Any]] = []
        self.metadata: Dict[str, Any] = {}

    def add_message(self, role: str, content: str, **kwargs):
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            **kwargs
        }
        self.messages.append(message)
        return message

    def get_messages(self, limit: int = None) -> List[Dict[str, Any]]:
        if limit:
            return self.messages[-limit:]
        return self.messages

    def clear(self):
        self.messages = []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "session_id": self.session_id,
            "created_at": self.created_at.isoformat(),
            "message_count": len(self.messages),
            "metadata": self.metadata
        }