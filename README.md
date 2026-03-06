🚀 NVIDIA Multi-Agent System (Microsoft Agent Framework Concepts)
A mini multi-agent system demonstrating core Microsoft Agent Framework architecture concepts using the NVIDIA NIM API (free LLM backend).

This project showcases how to build collaborative AI agents with session management, memory persistence, group chat orchestration, and concurrent agent execution.

It was developed as an internship learning project to understand how modern AI agent frameworks coordinate multiple intelligent agents to solve complex tasks.

🎯 Project Goals
The goal of this project is to understand and implement the core building blocks of modern AI agent systems, including:

Agent architecture

Session management

Context memory

Multi-agent collaboration

Parallel agent execution

LLM integration using NVIDIA NIM

🧠 Key Concepts Demonstrated
1️⃣ Agent System
Each agent acts as an independent AI unit capable of reasoning and generating responses using an LLM.

Example agents:

Research Agent

Writer Agent

Reviewer Agent

Legal Agent

Marketing Agent

2️⃣ Session Management
The AgentSession component manages conversation state across interactions.

Features:

Message history tracking

Timestamped interactions

Session isolation

Context persistence

3️⃣ Memory Provider
The MemoryProvider enables agents to remember user facts and preferences.

Capabilities:

Store persistent facts

Retrieve session-specific data

Inject memory into prompts

Context-aware responses

Example:

User: My name is Alex
Agent remembers → Alex
4️⃣ GroupChat Orchestration
The GroupChatOrchestrator allows multiple agents to collaborate on the same task.

Workflow example:

User Request
     ↓
Writer Agent
     ↓
Reviewer Agent
     ↓
Improved Output
Features:

Multi-agent collaboration

Round-robin speaker selection

Conversation history tracking

Termination conditions

5️⃣ Concurrent Orchestration
The ConcurrentOrchestrator runs multiple agents in parallel to generate diverse insights.

Example workflow:

User Request
      ↓
Research Agent
Marketing Agent
Legal Agent
      ↓
Aggregated Results
Benefits:

Faster processing

Multiple perspectives

Parallel execution

⚙️ Technologies Used
Python

NVIDIA NIM API

OpenAI-compatible API client

AsyncIO (parallel execution)

Environment variable security (.env)

Multi-agent architecture patterns

🏗️ Project Architecture
User Request
     ↓
NIMAgent (Base Agent Class)
     ↓
Session Manager
     ↓
Memory Injection
     ↓
LLM Processing (NVIDIA NIM)
     ↓
Response
Multi-agent orchestration layer:

                ┌──────────────────┐
                │  NVIDIA NIM LLM  │
                └─────────▲────────┘
                          │
                 ┌────────┴────────┐
                 │     NIMAgent    │
                 └────────▲────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
 ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
 │  Session    │   │  GroupChat  │   │ Concurrent  │
 │  + Memory   │   │ Orchestrator│   │ Orchestrator│
 └─────────────┘   └─────────────┘   └─────────────┘
📁 Project Structure
MAF/
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
🎬 Demo Modules
Demo	Description
Basic Agent	Single AI agent interacting with NVIDIA NIM
Session + Memory	Agent remembers user information
GroupChat	Two agents collaborate to refine output
Concurrent	Multiple expert agents analyze in parallel
🚀 Getting Started
1️⃣ Clone Repository
git clone https://github.com/your-username/nvidia-multi-agent-system.git
cd nvidia-multi-agent-system
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Add NVIDIA API Key
Create .env file:

NVIDIA_API_KEY=your_api_key
NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1
MODEL_ID=z-ai/glm-4-9b-0414
4️⃣ Run Demo
Run all demos:

python main.py
Run individual demo:

python demos/01_basic_agent.py
📊 Example Output
Example concurrent execution:

Researcher: Market demand for electric bikes is rapidly growing...
Marketer: The perfect eco-friendly solution for urban commuters...
Legal: Ensure compliance with regional transportation regulations...
🎓 Learning Outcomes
Through this project, the following concepts were explored:

AI agent architecture

Multi-agent orchestration

Parallel AI workflows

Context-aware LLM systems

Real-world AI system design patterns

🔮 Future Improvements
Potential extensions:

Vector database memory (RAG)

Tool calling agents

Web interface dashboard

Agent task routing

Persistent database sessions

Integration with Microsoft Agent Framework SDK

📚 References
NVIDIA NIM Platform

Microsoft Agent Framework

OpenAI API Specification

📜 License
Educational / Internship Learning Project
