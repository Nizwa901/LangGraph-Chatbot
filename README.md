# 🤖 LangGraph Multi-Tool AI Chatbot

A multi-tool AI chatbot built using LangGraph that handles general conversations, real-time weather queries, and mathematical calculations — all routed automatically based on user input.

Two versions are included:
- **AI Assistant** — Full modular LangGraph pipeline with three specialized tools
- **LangGraph Quickstart** — Minimal LangGraph agent using LangChain's built-in tool binding

---

## 🛠️ Tech Stack

| Tool / Library | Purpose |
|----------------|---------|
| Python | Core programming language |
| LangGraph | Graph-based agent workflow orchestration |
| Cohere API (`command-a-03-2025`) | Language model for chat and city spell correction |
| Weatherstack API | Real-time weather data retrieval |
| LangChain Cohere | Tool binding in the QuickStart version |
| python-dotenv | Secure API key management |
| requests | HTTP requests to Weatherstack API |

---

## 📁 Project Structure

```
LangGraph Projects/
├── AI Assistant/
│   ├── main.py              # Entry point — builds graph, runs chat loop
│   ├── state.py             # Defines shared state (AgentState)
│   ├── router.py            # Detects intent and routes to correct tool
│   ├── chatbot.py           # General conversation using Cohere
│   ├── weather_tool.py      # Fetches real-time weather data
│   ├── calculator_tool.py   # Performs math operations
│   ├── context_tool.py      # Passthrough node for input normalization
│   └── .env.example         # API key template
├── LangGraph Quickstart/
│   ├── main.py              # Minimal single-file agent
│   └── .env.example         # API key template
└── README.md
```

---

## 🔀 How It Works

### Graph Flow (AI Assistant)

```
User Input
    ↓
[context_rewriter]   → Passes input to the next node unchanged
    ↓
[router]             → Detects intent from keywords
    ↓
┌─────────────┬──────────────┬────────────┐
│ calculator  │   weather    │    chat    │
└─────────────┴──────────────┴────────────┘
      ↓               ↓             ↓
    [END]           [END]         [END]
```

### Routing Logic
- Math keywords (`add`, `plus`, `multiply`, `+`, `-`, etc.) → **calculator**
- Word `weather` → **weather**
- Everything else → **chat**

---

## ✨ Features

### 1. General Chat
- Powered by Cohere `command-a-03-2025`
- Maintains conversation history (last 10 messages)
- Understands follow-up questions naturally

### 2. Weather Tool
- Extracts city name from user query
- Auto-corrects misspelled city names using Cohere
- Fetches live data: temperature, humidity, wind speed, pressure, condition

### 3. Calculator Tool
- Handles addition, subtraction, multiplication, division
- Understands natural language: `"add 5 and 10"`, `"subtract 3 from 20"`
- Also evaluates direct expressions: `4 + 5 * 2`

---

## 🆚 AI Assistant vs QuickStart

| Feature | AI Assistant | QuickStart |
|---------|-------------|------------|
| Routing | Manual via `router.py` | Automatic via `tools_condition` |
| Files | 7 separate files | Single file |
| Tools | Chat, weather, calculator | Add only |
| State | Custom `AgentState` | Built-in `MessagesState` |
| Memory | Yes | No |

---

## ▶️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/Nizwa901/LangGraph-Chatbot.git
   cd "LangGraph Projects"
   ```

2. **Install dependencies**
   ```bash
   pip install langgraph langchain-cohere cohere python-dotenv requests
   ```

3. **Set up environment variables**
   ```bash
   cp "AI Assistant/.env.example" "AI Assistant/.env"
   ```
   Then open `.env` and add your API keys.

4. **Run the AI Assistant**
   ```bash
   cd "AI Assistant"
   python main.py
   ```

---

## 🔐 Security

- All API keys stored in `.env` file
- `.env` excluded from version control via `.gitignore`
- `.env.example` provided with placeholder values

---

## 👤 Author

**Nizwa KP**
B.Tech Computer Science Engineering (AI & ML)
APJ Abdul Kalam Technological University (KTU)

*Documented on 10 June 2026*
