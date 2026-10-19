# weather.py

import requests


def get_weather_description(code):
    """Convert a weather code into a readable description."""
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Heavy drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Rain showers",
        81: "Moderate rain showers",
        82: "Heavy rain showers",
        95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Heavy thunderstorm with hail"
    }

    return descriptions.get(code, "Unknown weather condition")


def get_weather():
    city = input("Enter a city name: ").strip()

    if not city:
        print("Error: City name cannot be empty.")
        return

    try:
        # Step 1: Find the city coordinates
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_response = requests.get(
            geo_url,
            params={"name": city, "count": 1, "language": "en"},
            timeout=10
        )
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        results = geo_data.get("results", [])

        if not results:
            print("Error: City not found. Check the spelling.")
            return

        location = results[0]
        latitude = location["latitude"]
        longitude = location["longitude"]

        # Step 2: Get the current weather
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_response = requests.get(
            weather_url,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,weather_code",
                "temperature_unit": "fahrenheit",
                "timezone": "auto"
            },
            timeout=10
        )
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data["current"]
        temperature = current["temperature_2m"]
        code = current["weather_code"]
        description = get_weather_description(code)

        # Step 3: Display the results
        print("\n--- Current Weather ---")
        print(f"City: {location['name']}")
        print(f"Temperature: {temperature} °F")
        print(f"Conditions: {description}")

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect. Check your internet connection.")

    except requests.exceptions.HTTPError:
        print("Error: The weather service returned an unsuccessful response.")

    except requests.exceptions.RequestException as error:
        print(f"Network error: {error}")

    except (KeyError, ValueError):
        print("Error: Received invalid or incomplete weather data.")


if __name__ == "__main__":
    get_weather()