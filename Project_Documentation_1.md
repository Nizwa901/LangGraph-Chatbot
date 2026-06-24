# Project Documentation

## LangGraph Multi-Tool AI Chatbot

**Author:** Nizwa

**Technology:** Python, LangGraph, Cohere API, Weatherstack API

**Type:** Conversational AI Agent

---

## Overview

This project is a multi-tool AI chatbot built using LangGraph, a graph-based framework for orchestrating AI workflows. The chatbot can handle general conversations, answer real-time weather queries, and perform mathematical calculations — all routed automatically based on the user's input.

Two versions were developed:

- **Full Project** — A modular, multi-node LangGraph pipeline with three specialized tools
- **QuickStart** — A minimal LangGraph agent using LangChain's built-in tool binding

---

## Tools and Technologies Used

| Tool / Library | Purpose |
|----------------|---------|
| Python | Core programming language |
| LangGraph | Graph-based agent workflow orchestration |
| Cohere API (`command-a-03-2025`) | Language model for chat and city spell correction |
| Weatherstack API | Real-time weather data retrieval |
| LangChain Cohere | Tool binding in the QuickStart version |
| python-dotenv | Secure API key management via `.env` file |
| requests | HTTP requests to the Weatherstack API |

---

## Project Structure

The full project is split into separate files, each handling one responsibility:

| File | Responsibility |
|------|---------------|
| `main.py` | Entry point — builds the graph, runs the chat loop |
| `state.py` | Defines the shared state structure (`AgentState`) |
| `router.py` | Detects user intent and routes to the correct tool |
| `chatbot.py` | Handles general conversation using Cohere |
| `weather_tool.py` | Fetches real-time weather data |
| `calculator_tool.py` | Performs math operations |
| `context_tool.py` | Passthrough node for input normalization |

---

## How It Works

### Graph Flow

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

The router reads the user's input and decides which node to activate:

- If the input contains math keywords (`add`, `plus`, `multiply`, `+`, `-`, etc.) → routed to **calculator**
- If the input contains the word `weather` → routed to **weather**
- Everything else → routed to **chat**

---

## Features

### 1. General Chat (`chatbot.py`)
- Powered by Cohere's `command-a-03-2025` model
- Maintains conversation history (last 10 messages)
- Understands follow-up questions naturally (e.g., "give examples", "its", "explain more")
- Does not repeat greetings unnecessarily

### 2. Weather Tool (`weather_tool.py`)
- Extracts the city name from the user's query
- Auto-corrects misspelled city names using Cohere
- Fetches live weather data from Weatherstack API
- Returns temperature, humidity, wind speed, pressure, and weather condition

### 3. Calculator Tool (`calculator_tool.py`)
- Handles addition, subtraction, multiplication, and division
- Understands natural language (e.g., "add 5 and 10", "subtract 3 from 20")
- Also evaluates direct expressions (e.g., `4 + 5 * 2`)

---

## QuickStart Version

A simpler, beginner-friendly version of the chatbot built using LangChain's tool binding feature.

### What It Does
- Takes a user message and passes it to the Cohere model
- If the model decides a tool is needed, it calls the tool automatically
- After getting the tool result, the model responds to the user

### Graph Flow

```
User Message
    ↓
[chatbot node]       → Cohere model processes the message
    ↓
[tools_condition]    → Checks if a tool call is needed
    ↓
[ToolNode]           → Executes the tool (e.g., add two numbers)
    ↓
[chatbot node]       → Model sees the result and gives final response
```

### Tool Defined
- `add(a, b)` — adds two numbers, bound to the Cohere model using LangChain

### Key Difference from Full Project

| Full Project | QuickStart |
|-------------|------------|
| Manual routing via `router.py` | Automatic routing via `tools_condition` |
| 7 separate files | Single file |
| 3 tools (chat, weather, calculator) | 1 tool (add) |
| Custom state (`AgentState`) | Built-in `MessagesState` |
| Conversation memory | No memory between turns |

---

## Security

- All API keys are stored in a `.env` file
- `.env` is excluded from version control using `.gitignore`
- A `.env.example` file is provided with placeholder values for reference

---

## What Was Learned

- How to design a stateful multi-node graph using LangGraph
- How to route user intent to specialized tool nodes
- How to maintain conversation memory across turns
- How to integrate external APIs (weather) inside a graph node
- How to use Cohere for both chat and utility tasks (spell correction)
- Best practices for API key security using environment variables

---

*Documented on 10 June 2026*
