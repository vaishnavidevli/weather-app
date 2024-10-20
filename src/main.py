import time
from weather_api import fetch_weather_data
from data_processor import process_weather_data, generate_daily_summary

API_KEY = 'e52aef32f94d9748d6e861d1b1a6cc44'  # Replace with your actual API key
LOCATIONS = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
INTERVAL = 300  # 5 minutes in seconds

def main():
    while True:
        for location in LOCATIONS:
            weather_data = fetch_weather_data(location, API_KEY)
            if weather_data:
                process_weather_data(weather_data)
                generate_daily_summary()
        time.sleep(INTERVAL)

if __name__ == '__main__':
    main()
