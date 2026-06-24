from langchain_cohere import ChatCohere
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition
import os
from dotenv import load_dotenv
load_dotenv()


# Define the tool
@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


# List of tools
tools = [add]


# Initialize the model and bind tools
model = ChatCohere(
    model="command-a-03-2025",
    cohere_api_key = os.getenv("COHERE_API_KEY")
).bind_tools(tools)


# Define chatbot node
def chatbot(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": [response]}


# Build graph
graph_builder = StateGraph(MessagesState)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tools))

graph_builder.add_edge(START, "chatbot")

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition
)

graph_builder.add_edge("tools", "chatbot")

# Compile graph
graph = graph_builder.compile()


# Chat loop
print("AI: Hello! How can I help you today?")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        print("AI: Goodbye!")
        break

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=user_input)
            ]
        }
    )

    print("AI:", result["messages"][-1].content)