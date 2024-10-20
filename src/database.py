

import requests
import sqlite3
import time
from flask import Flask, render_template

API_KEY = 'e52aef32f94d9748d6e861d1b1a6cc44'  # Replace with your actual API key
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
DB_NAME = 'weather_data.db'

app = Flask(__name__)

def get_weather_data(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

def process_weather_data(data):
    city = data['name']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    condition = data['weather'][0]['main']
    return city, temperature, humidity, condition

def save_weather_data(city, temperature, humidity, condition):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL,
        temperature REAL NOT NULL,
        humidity REAL NOT NULL,
        condition TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    );''')
    cursor.execute('INSERT INTO weather (city, temperature, humidity, condition) VALUES (?, ?, ?, ?)',
                   (city, temperature, humidity, condition))
    conn.commit()
    conn.close()

def update_weather_data():
    while True:
        for city in CITIES:
            weather_data = get_weather_data(city)
            if weather_data.get('cod') == 200:
                city, temperature, humidity, condition = process_weather_data(weather_data)
                save_weather_data(city, temperature, humidity, condition)
                print(f"Data saved for {city}: {temperature}°C, {humidity}%, Condition: {condition}")
        time.sleep(300)  # Sleep for 5 minutes

@app.route('/')
def index():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM weather ORDER BY timestamp DESC')
    rows = cursor.fetchall()
    conn.close()
    return render_template('index.html', weather_data=rows)

if __name__ == "__main__":
    import threading
    threading.Thread(target=update_weather_data, daemon=True).start()  # Run weather update in the background
    app.run(debug=True)

# 5555import requests
# import sqlite3
# import time
#
# API_KEY = 'e52aef32f94d9748d6e861d1b1a6cc44'  # Replace with your actual API key
# CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
# DB_NAME = 'weather_data.db'
#
# def get_weather_data(city):
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
#     response = requests.get(url)
#     return response.json()
#
# def process_weather_data(data):
#     city = data['name']
#     temperature = data['main']['temp']
#     humidity = data['main']['humidity']
#     condition = data['weather'][0]['main']
#     return city, temperature, humidity, condition
#
# def save_weather_data(city, temperature, humidity, condition):
#     conn = sqlite3.connect(DB_NAME)
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
#     while True:
#         for city in CITIES:
#             weather_data = get_weather_data(city)
#             if weather_data.get('cod') == 200:
#                 city, temperature, humidity, condition = process_weather_data(weather_data)
#                 save_weather_data(city, temperature, humidity, condition)
#                 print(f"Data saved for {city}: {temperature}°C, {humidity}%, Condition: {condition}")
#         time.sleep(300)  # Sleep for 5 minutes
#
# if __name__ == "__main__":
#     main()

















#
#
# import requests
# import sqlite3
# import time
#
# API_KEY = 'e52aef32f94d9748d6e861d1b1a6cc44'  # Replace with your actual API key
# CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
# DB_NAME = 'weather_data.db'
#
# def get_weather_data(city):
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
#     response = requests.get(url)
#     return response.json()
#
# def process_weather_data(data):
#     # Extract relevant information
#     city = data['name']
#     temperature = data['main']['temp']  # Already in Celsius since we use 'units=metric'
#     humidity = data['main']['humidity']
#     condition = data['weather'][0]['main']
#     return city, temperature, humidity, condition
#
# def save_weather_data(city, temperature, humidity, condition):
#     conn = sqlite3.connect(DB_NAME)
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
#     while True:
#         for city in CITIES:
#             weather_data = get_weather_data(city)
#             if weather_data.get('cod') == 200:
#                 city, temperature, humidity, condition = process_weather_data(weather_data)
#                 save_weather_data(city, temperature, humidity, condition)
#                 print(f"Data saved for {city}: {temperature}°C, {humidity}%, Condition: {condition}")
#             else:
#                 print(f"Failed to retrieve data for {city}: {weather_data.get('message')}")
#         time.sleep(300)  # Sleep for 5 minutes
#
# if __name__ == "__main__":
#     main()



# import requests
# import sqlite3
# import time
#
# API_KEY = 'your_api_key'  # Replace with your actual API key
# CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
# DB_NAME = 'weather_data.db'
#
# def get_weather_data(city):
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
#     response = requests.get(url)
#     return response.json()
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
#     conn = sqlite3.connect(DB_NAME)
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
#     while True:
#         for city in CITIES:
#             weather_data = get_weather_data(city)
#             if weather_data.get('cod') == 200:
#                 city, temperature, humidity, condition = process_weather_data(weather_data)
#                 save_weather_data(city, temperature, humidity, condition)
#                 print(f"Data saved for {city}: {temperature}°C, {humidity}%, Condition: {condition}")
#         time.sleep(300)  # Sleep for 5 minutes
#
# if __name__ == "__main__":
#     main()































# import sqlite3
# import signal
# import sys
# import time
# import requests
#
# def signal_handler(sig, frame):
#     print('Exiting gracefully...')
#     sys.exit(0)
#
# def fetch_weather_data(location, api_key):
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Failed to fetch data for {location}: {response.status_code}, {response.text}")
#         return None
#
# def setup_database():
#     conn = sqlite3.connect('weather_data.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS daily_summaries (
#             date TEXT,
#             avg_temp REAL,
#             max_temp REAL,
#             min_temp REAL,
#             dominant_condition TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()
#     print("Database setup complete.")
#
# def process_daily_data(weather_updates):
#     if not weather_updates:
#         print("No weather updates to process.")
#         return
#
#     avg_temp = sum(update['temp'] for update in weather_updates) / len(weather_updates)
#     max_temp = max(update['temp'] for update in weather_updates)
#     min_temp = min(update['temp'] for update in weather_updates)
#     dominant_condition = max(weather_updates, key=lambda x: weather_updates.count(x['main']))['main']
#
#     print(f"Daily Summary: Avg Temp: {avg_temp:.2f}°C, Max Temp: {max_temp:.2f}°C, Min Temp: {min_temp:.2f}°C, Dominant Condition: {dominant_condition}")
#
#     # Here you would typically store the summary in the database
#     # store_daily_summary(date, avg_temp, max_temp, min_temp, dominant_condition)
#
# def main():
#     api_key = 'e52aef32f94d9748d6e861d1b1a6cc44'  # Replace with your actual API key
#     locations = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
#     weather_updates = []
#
#     setup_database()  # Set up the database
#
#     # Register the signal handler
#     signal.signal(signal.SIGINT, signal_handler)
#
#     while True:
#         for location in locations:
#             print(f"Fetching weather data for {location}...")
#             weather_data = fetch_weather_data(location, api_key)
#             if weather_data:
#                 # Convert temperature from Kelvin to Celsius
#                 temp = weather_data['main']['temp'] - 273.15  # Kelvin to Celsius
#                 weather_updates.append({'temp': temp, 'main': weather_data['weather'][0]['main']})
#                 print(f"Weather in {location}: {temp:.2f}°C, Condition: {weather_data['weather'][0]['main']}")
#
#         # Process daily data every 24 hours (you might want to adjust this logic)
#         if len(weather_updates) >= len(locations):
#             process_daily_data(weather_updates)
#             weather_updates.clear()  # Clear the list for the next day
#             print("Daily weather summary processed.")
#
#         time.sleep(300)  # Wait for 5 minutes before the next API call
#
# if __name__ == "__main__":
#     main()

# import sqlite3
# import requests
# import time
# from datetime import datetime, timedelta
#
# # Function to set up the database
# def setup_database():
#     conn = sqlite3.connect('weather_data.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS daily_summaries (
#             date TEXT PRIMARY KEY,
#             avg_temp REAL,
#             max_temp REAL,
#             min_temp REAL,
#             dominant_condition TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()
#
# # Function to store daily summary in the database
# def store_daily_summary(date, avg_temp, max_temp, min_temp, dominant_condition):
#     conn = sqlite3.connect('weather_data.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         INSERT OR REPLACE INTO daily_summaries (date, avg_temp, max_temp, min_temp, dominant_condition)
#         VALUES (?, ?, ?, ?, ?)
#     ''', (date, avg_temp, max_temp, min_temp, dominant_condition))
#     conn.commit()
#     conn.close()
#
# # Function to fetch weather data from OpenWeatherMap API
# def fetch_weather_data(location, api_key):
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Failed to fetch data for {location}: {response.status_code}, {response.text}")
#         return None
#
# # Function to process daily weather data and store summary
# def process_daily_data(weather_updates):
#     total_temp = sum(update['temp'] for update in weather_updates)
#     max_temp = max(update['temp'] for update in weather_updates)
#     min_temp = min(update['temp'] for update in weather_updates)
#     avg_temp = total_temp / len(weather_updates)
#
#     # Determine the dominant weather condition
#     conditions = [update['main'] for update in weather_updates]
#     dominant_condition = max(set(conditions), key=conditions.count)
#
#     # Store the summary in the database
#     date = datetime.now().strftime('%Y-%m-%d')
#     store_daily_summary(date, avg_temp, max_temp, min_temp, dominant_condition)
#
# # Main function to run the weather monitoring system
# def main():
#     api_key = 'e52aef32f94d9748d6e861d1b1a6cc44'  # Replace with your actual API key
#     locations = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
#     weather_updates = []
#
#     setup_database()  # Set up the database
#
#     while True:
#         for location in locations:
#             weather_data = fetch_weather_data(location, api_key)
#             if weather_data:
#                 # Convert temperature from Kelvin to Celsius
#                 temp = weather_data['main']['temp'] - 273.15  # Kelvin to Celsius
#                 weather_updates.append({'temp': temp, 'main': weather_data['weather'][0]['main']})
#
#         # Process daily data every 24 hours
#         if len(weather_updates) >= len(locations):
#             process_daily_data(weather_updates)
#             weather_updates.clear()  # Clear the list for the next day
#
#         time.sleep(300)  # Wait for 5 minutes before the next API call
#
# if __name__ == "__main__":
#     main()





# import sqlite3
#
# def setup_database():
#     conn = sqlite3.connect('weather_data.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS daily_summaries (
#             date TEXT,
#             avg_temp REAL,
#             max_temp REAL,
#             min_temp REAL,
#             dominant_condition TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()
#
# def store_daily_summary(date, avg_temp, max_temp, min_temp, dominant_condition):
#     conn = sqlite3.connect('weather_data.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         INSERT INTO daily_summaries (date, avg_temp, max_temp, min_temp, dominant_condition)
#         VALUES (?, ?, ?, ?, ?)
#     ''', (date, avg_temp, max_temp, min_temp, dominant_condition))
#     conn.commit()
#     conn.close()
