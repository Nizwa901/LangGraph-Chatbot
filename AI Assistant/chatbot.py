import cohere
import os
from dotenv import load_dotenv
load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))


def chat_node(state):

    query = state["user_input"].strip()

    messages = state.get("messages", [])

    # Keep last 10 messages
    history_text = "\n".join(
        [f"{m['role']}: {m['content']}" for m in messages[-10:]]
    )

    prompt = f"""
You are a helpful AI assistant.

Rules:
- Always use the conversation history.
- If the user says:
    its
    this
    that
    these
    those
    examples
    applications
    advantages
    disadvantages
    explain more
    tell me more
    yes
  then continue from the previous topic.

- Understand follow-up questions naturally.
- If the user greets, answer simply.
- Do not write 'AI:'.
- Be concise unless more detail is requested.

Conversation History:
{history_text}

Current User Question:
{query}
"""

    response = co.chat(
        model="command-a-03-2025",
        message=prompt
    )

    answer = response.text.strip()

    # Save memory
    messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    return {
        "response": answer,
        "messages": messages
    }
