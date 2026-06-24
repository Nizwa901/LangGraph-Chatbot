import re


def calculator_node(state):

    query = state["user_input"].lower()

    try:

        # Addition
        if "add" in query or "plus" in query:

            numbers = list(map(float, re.findall(r'\d+\.?\d*', query)))

            result = numbers[0] + numbers[1]

            response = (
                f"The sum of {int(numbers[0])} and {int(numbers[1])} is {result:g}."
            )

        # Subtraction
        elif "subtract" in query or "substract" in query or "minus" in query:

            numbers = list(map(float, re.findall(r'\d+\.?\d*', query)))

            if "from" in query:
                result = numbers[1] - numbers[0]
                response = (
                    f"The difference between {int(numbers[1])} and "f"{int(numbers[0])} is {result:g}."
                )
            else:
                result = numbers[0] - numbers[1]
                response = (
                     f"The difference between {int(numbers[0])} and "f"{int(numbers[1])} is {result:g}."
                )

        # Multiplication
        elif "multiply" in query or "times" in query:

            numbers = list(map(float, re.findall(r'\d+\.?\d*', query)))

            result = numbers[0] * numbers[1]

            response = (
                f"The product of {int(numbers[0])} and {int(numbers[1])} is {result:g}."
            )

        # Division
        elif "divide" in query:

            numbers = list(map(float, re.findall(r'\d+\.?\d*', query)))

            result = numbers[0] / numbers[1]

            response = (
                f"Dividing {int(numbers[0])} by {int(numbers[1])} gives {result:g}."
            )

        # Direct expressions like 4+5
        else:

            result = eval(query)

            response = f"The answer is {result:g}."

    except:

        response = "Sorry, I could not understand the calculation."

    return {
        "response": response
    }
