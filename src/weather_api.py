# import requests
# import sqlite3
# import time
#
# def fetch_weather_data(location, api_key):
#     # Construct the API request URL
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
#     print(f"Fetching weather data from: {url}")  # Debugging line
#
#     try:
#         response = requests.get(url)
#         print(f"Response Code: {response.status_code}")  # Debugging line
#
#         # Check if the request was successful
#         if response.status_code == 200:
#             return response.json()
#         else:
#             print(f"Failed to fetch data for {location}: {response.status_code}, {response.text}")
#             return None
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
#         return None
#
# def process_weather_data(data):
#     # Extract relevant information
#     city = data['name']
#     temperature = data['main']['temp']
#     humidity = data['main']['humidity']
#     condition = data['weather'][0]['main']
#     return city, temperature, humidity, condition
#
# def save_weather_data(city, temperature, humidity, condition):
#     conn = sqlite3.connect('weather_data.db')  # Ensure this matches your database file
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         city TEXT NOT NULL,
#         temperature REAL NOT NULL,
#         humidity REAL NOT NULL,
#         condition TEXT NOT NULL,
#         timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
#     );''')
#     cursor.execute('INSERT INTO weather (city, temperature, humidity, condition) VALUES (?, ?, ?, ?)',
#                    (city, temperature, humidity, condition))
#     conn.commit()
#     conn.close()
#
# def main():
#     api_key = 'e52aef32f94d9748d6e861d1b1a6cc44cd '  # Replace with your actual API key
#     cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
#
#     while True:
#         for city in cities:
#             weather_data = fetch_weather_data(city, api_key)
#             if weather_data:
#                 city, temperature, humidity, condition = process_weather_data(weather_data)
#                 save_weather_data(city, temperature, humidity, condition)
#                 print(f"Data saved for {city}: {temperature}°C, {humidity}%, Condition: {condition}")
#         time.sleep(300)  # Sleep for 5 minutes
#
# if __name__ == "__main__":
#     main()
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def fetch_weather_data(location, api_key):
    """Fetch weather data from OpenWeatherMap API."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    logging.info(f"Fetching weather data from: {url}")

    try:
        response = requests.get(url)
        logging.info(f"Response Code: {response.status_code}")

        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Failed to fetch data for {location}: {response.status_code}, {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return None

def process_weather_data(data):
    """Process the fetched weather data."""
    if not data:
        logging.warning("No data to process.")
        return None

    try:
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['main']

        return {
            'city': city,
            'temperature': temperature,
            'humidity': humidity,
            'condition': condition
        }
    except KeyError as e:
        logging.error(f"Key error: {e} - possibly the data format has changed.")
        return None

def display_weather_info(processed_data):
    """Display the processed weather information."""
    if processed_data:
        print(f"Weather in {processed_data['city']}: {processed_data['temperature']}°C, "
              f"Humidity: {processed_data['humidity']}%, Condition: {processed_data['condition']}")
    else:
        print("No weather data to display.")

if __name__ == "__main__":
    api_key = 'e52aef32f94d9748d6e861d1b1a6cc44'  # Replace with your actual API key
    location = input("Enter the city name: ")  # Prompt user for city name

    weather_data = fetch_weather_data(location, api_key)
    processed_data = process_weather_data(weather_data)

    display_weather_info(processed_data)








#
#4444 import requests
#
#
# def fetch_weather_data(location, api_key):
#     # Construct the API request URL
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
#     print(f"Fetching weather data from: {url}")  # Debugging line
#
#     try:
#         response = requests.get(url)
#         print(f"Response Code: {response.status_code}")  # Debugging line
#
#         # Check if the request was successful
#         if response.status_code == 200:
#             return response.json()
#         else:
#             print(f"Failed to fetch data for {location}: {response.status_code}, {response.text}")
#             return None
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
#         return None
#
#
# def process_weather_data(data):
#     """Process the fetched weather data."""
#     if not data:
#         print("No data to process.")
#         return None
#
#     try:
#         city = data['name']
#         temperature = data['main']['temp']
#         humidity = data['main']['humidity']
#         condition = data['weather'][0]['main']
#
#         weather_info = {
#             'city': city,
#             'temperature': temperature,
#             'humidity': humidity,
#             'condition': condition
#         }
#
#         return weather_info
#     except KeyError as e:
#         print(f"Key error: {e} - possibly the data format has changed.")
#         return None
#
#
# # Example usage
# if __name__ == "__main__":
#     api_key = 'e52aef32f94d9748d6e861d1b1a6cc44'  # Replace with your actual API key
#     location = 'Delhi'  # Replace with your desired location
#
#     weather_data = fetch_weather_data(location, api_key)
#     processed_data = process_weather_data(weather_data)
#
#     if processed_data:
#         print(f"Weather in {processed_data['city']}: {processed_data['temperature']}°C, "
#               f"Humidity: {processed_data['humidity']}%, Condition: {processed_data['condition']}")
#
# #2 import requests
# #
#
# def fetch_weather_data(location, api_key):
#     # Construct the API request URL
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
#     print(f"Fetching weather data from: {url}")  # Debugging line
#
#     try:
#         response = requests.get(url)
#         print(f"Response Code: {response.status_code}")  # Debugging line
#
#         # Check if the request was successful
#         if response.status_code == 200:
#             return response.json()
#         else:
#             print(f"Failed to fetch data for {location}: {response.status_code}, {response.text}")
#             return None
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
#         return None
#
#
# # Example usage
# if __name__ == "__main__":
#     api_key = 'e52aef32f94d9748d6e861d1b1a6cc44'  # Replace with your actual API key
#     location = 'Delhi'  # Replace with your desired location
#
#     weather_data = fetch_weather_data(location, api_key)
#     if weather_data:
#         print(weather_data)  # Print or process the fetched weather data
