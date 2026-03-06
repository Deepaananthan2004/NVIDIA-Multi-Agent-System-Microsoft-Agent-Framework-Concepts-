🚀 NVIDIA Multi-Agent System
A mini multi-agent AI system demonstrating core Microsoft Agent Framework concepts using the NVIDIA NIM API (LLM backend).

This project shows how multiple AI agents can collaborate, remember context, and work in parallel to solve tasks using modern agent orchestration patterns.

📌 Features
Feature	Description
🤖 Agent System	Modular AI agents using NVIDIA NIM API
💬 Session Management	Maintains conversation state across requests
🧠 Memory Provider	Stores user facts and context
👥 GroupChat Orchestration	Agents collaborate to solve a task
⚡ Concurrent Execution	Multiple agents run tasks in parallel
🔐 Secure API Handling	Uses .env for API key protection
🏗️ Architecture
User Request
      │
      ▼
 ┌───────────────┐
 │   NIMAgent    │
 │ (Base Agent)  │
 └───────▲───────┘
         │
 ┌───────┼───────────────┐
 │       │               │
 ▼       ▼               ▼

Session   Memory    NVIDIA NIM API
Manager   Provider      (LLM)

         │
         ▼

 ┌──────────────────────────────┐
 │  Agent Orchestration Layer   │
 │                              │
 │  • GroupChat Orchestrator    │
 │  • Concurrent Orchestrator   │
 └──────────────────────────────┘
📂 Project Structure
MAF/
│
├── core/
│   ├── agent.py
│   ├── session.py
│   └── memory.py
│
├── orchestrations/
│   ├── groupchat.py
│   └── concurrent.py
│
├── demos/
│   ├── 01_basic_agent.py
│   ├── 02_session_memory.py
│   ├── 03_groupchat.py
│   └── 04_concurrent.py
│
├── .env
├── requirements.txt
├── main.py
└── README.md
⚙️ Technologies Used
Python

NVIDIA NIM API

AsyncIO

OpenAI-compatible API

Environment Variables (.env)

🚀 Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/nvidia-multi-agent-system.git
cd nvidia-multi-agent-system
2️⃣ Create Virtual Environment
python -m venv venv
Activate environment:

Windows

venv\Scripts\activate
Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure NVIDIA API
Create a .env file in the project root.

NVIDIA_API_KEY=your_api_key_here
NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1
MODEL_ID=z-ai/glm-4-9b-0414
Get your key from:

https://build.nvidia.com

▶️ Running the Project
Run the full demo suite:

python main.py
Run individual demos:

python demos/01_basic_agent.py
python demos/02_session_memory.py
python demos/03_groupchat.py
python demos/04_concurrent.py
🎬 Demo Overview
Demo	Description
Basic Agent	Simple AI agent interaction
Session + Memory	Agent remembers user data
GroupChat	Multiple agents collaborate
Concurrent	Parallel agent task execution
🧠 Example Workflow
User Prompt
     │
     ▼
Agent System
     │
     ▼
GroupChat / Concurrent Execution
     │
     ▼
NVIDIA NIM LLM Processing
     │
     ▼
Aggregated Response
🎓 Learning Outcomes
This project demonstrates:

Multi-agent system design

Agent orchestration patterns

Session-based AI applications

Context-aware AI agents

Parallel AI task execution

🔮 Future Improvements
Possible enhancements:

Vector database memory (RAG)

Tool calling agents

Web UI dashboard

Persistent database sessions

Integration with Microsoft Agent Framework SDK

📚 References
NVIDIA NIM Platform

Microsoft Agent Framework

OpenAI API Documentation

📜 License
Educational / Internship Learning Project

