import requests
import cohere
import os
from dotenv import load_dotenv
load_dotenv()

# Weatherstack API key
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Cohere API key
co = cohere.Client(os.getenv("COHERE_API_KEY"))


def extract_city(query):

    query = query.lower()

    query = query.replace("what is the weather in", "")
    query = query.replace("weather in", "")
    query = query.replace("what's the weather in", "")

    return query.strip()


def correct_city(city):

    prompt = f"""
Correct the spelling of this city name.

City: {city}

Return only the corrected city name.
Do not give explanations.
"""

    response = co.chat(
        model="command-a-03-2025",
        message=prompt
    )

    corrected_city = response.text.strip()

    return corrected_city


def weather_node(state):

    raw_query = state["user_input"]

    original_city = extract_city(raw_query)

    corrected_city = correct_city(original_city)

    url = (
        f"http://api.weatherstack.com/current"
        f"?access_key={WEATHER_API_KEY}"
        f"&query={corrected_city}"
    )

    data = requests.get(url).json()

    if "current" not in data:

        return {
            "response": (
                f"Sorry, I couldn't find weather information "
                f"for '{original_city}'. Please check the spelling."
            )
        }

    current = data["current"]
    location = data["location"]

    city_name = location["name"]
    region = location["region"]
    country = location["country"]

    temp = current["temperature"]
    humidity = current["humidity"]
    wind = current["wind_speed"]
    pressure = current["pressure"]

    weather_desc = ", ".join(
        current["weather_descriptions"]
    )

    response = ""

    if original_city.lower() != corrected_city.lower():

        response += (
            f"The corrected city name is {corrected_city}.\n"
        )

    response += (
        f"The city is {city_name}.\n"
        f"It is located in the state of {region}.\n"
        f"The country is {country}.\n"
        f"The current temperature is {temp} °C.\n"
        f"The humidity is {humidity} percent.\n"
        f"The wind speed is {wind} km/h.\n"
        f"The atmospheric pressure is {pressure} mb.\n"
        f"The weather condition is {weather_desc}."
    )

    return {
        "response": response,
        "messages": state.get("messages", [])
    }
