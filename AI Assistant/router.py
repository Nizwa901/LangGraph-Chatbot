def route(state):

    query = state["user_input"].lower()

    # Calculator detection
    calculator_keywords = [
        "+", "-", "*", "/", "×", "÷",
        "add", "plus",
        "subtract", "minus",
        "multiply", "times",
        "divide"
    ]

    if any(word in query for word in calculator_keywords):
        return "calculator"

    # Weather detection
    elif "weather" in query:
        return "weather"

    # Default → Chatbot
    else:
        return "chat"