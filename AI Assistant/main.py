from langgraph.graph import StateGraph, START, END

from state import AgentState
from context_tool import context_rewriter
from router import route

from calculator_tool import calculator_node
from weather_tool import weather_node
from chatbot import chat_node


# Create graph
builder = StateGraph(AgentState)

# Add nodes
builder.add_node("context", context_rewriter)
builder.add_node("calculator", calculator_node)
builder.add_node("weather", weather_node)
builder.add_node("chat", chat_node)

# START → context
builder.add_edge(START, "context")

# context → route
builder.add_conditional_edges(
    "context",
    route
)

# End nodes
builder.add_edge("calculator", END)
builder.add_edge("weather", END)
builder.add_edge("chat", END)

# Compile graph
graph = builder.compile()


# ==========================
# Conversation Memory
# ==========================
messages = []


# Chat Loop
while True:

    user_input = input("User: ")

    if user_input.lower() == "exit":
        print("\nAI: Goodbye!")
        break

    result = graph.invoke(
        {
            "user_input": user_input,
            "response": "",
            "messages": messages
        }
    )

    # Save updated memory
    messages = result.get("messages", messages)

    print("\nAI:", result["response"])