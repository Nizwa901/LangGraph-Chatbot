def context_rewriter(state):

    user_input = state["user_input"]

    # Simply pass the input unchanged
    return {
        "user_input": user_input,
        "messages": state.get("messages", []),
        "response": state.get("response", "")
    }
