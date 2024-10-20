# 44444import pandas as pd
#
# weather_data_storage = []
#
#
# def convert_kelvin_to_celsius(kelvin):
#     return kelvin - 273.15
#
#
# def process_weather_data(data):
#     main = data['main']
#     weather = data['weather'][0]
#
#     current_temp = convert_kelvin_to_celsius(main['temp'])
#     feels_like_temp = convert_kelvin_to_celsius(main['feels_like'])
#
#     weather_data_storage.append({
#         'main_condition': weather['main'],
#         'current_temp': current_temp,
#         'feels_like_temp': feels_like_temp,
#         'dt': data['dt']
#     })
#
#
# def generate_daily_summary():
#     # Convert stored data to a DataFrame
#     df = pd.DataFrame(weather_data_storage)
#
#     # Daily aggregates (example aggregation logic)
#     daily_summary = df.groupby(df['dt'].apply(lambda x: pd.to_datetime(x, unit='s').date())).agg({
#         'current_temp': ['mean', 'max', 'min'],
#         'main_condition': lambda x: x.mode()[0]  # Dominant condition
#     })
#
#     print(daily_summary)
#     # Store in a database (implementation needed)

# import pandas as pd
# import sqlite3
#
# # Global list to store weather data
# weather_data_storage = []
#
#
# def convert_kelvin_to_celsius(kelvin):
#     """Convert Kelvin to Celsius."""
#     return kelvin - 273.15
#
#
# def process_weather_data(data):
#     """Process the fetched weather data."""
#     main = data['main']
#     weather = data['weather'][0]
#
#     current_temp = convert_kelvin_to_celsius(main['temp'])
#     feels_like_temp = convert_kelvin_to_celsius(main['feels_like'])
#
#     # Append processed data to storage
#     weather_data_storage.append({
#         'main_condition': weather['main'],
#         'current_temp': current_temp,
#         'feels_like_temp': feels_like_temp,
#         'dt': data['dt']
#     })
#
#
# def generate_daily_summary():
#     """Generate daily summary from stored weather data."""
#     # Convert stored data to a DataFrame
#     df = pd.DataFrame(weather_data_storage)
#
#     if df.empty:
#         print("No weather data available for summary.")
#         return
#
#     # Convert 'dt' to datetime
#     df['dt'] = pd.to_datetime(df['dt'], unit='s')
#
#     # Daily aggregates
#     daily_summary = df.groupby(df['dt'].dt.date).agg({
#         'current_temp': ['mean', 'max', 'min'],
#         'main_condition': lambda x: x.mode()[0]  # Dominant condition
#     })
#
#     # Print the daily summary
#     print("Daily Weather Summary:")
#     for date, row in daily_summary.iterrows():
#         print(f"Date: {date}, Mean Temp: {row['current_temp']['mean']:.2f}°C, "
#               f"Max Temp: {row['current_temp']['max']:.2f}°C, "
#               f"Min Temp: {row['current_temp']['min']:.2f}°C, "
#               f"Dominant Condition: {row['main_condition'][0]}")
#
#     # Store in a database
#     store_daily_summary(daily_summary)
#
#
# def store_daily_summary(daily_summary):
#     """Store daily summary in SQLite database."""
#     conn = sqlite3.connect('weather_summary.db')
#     cursor = conn.cursor()
#
#     # Create table if it doesn't exist
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS daily_weather_summary (
#         date DATE PRIMARY KEY,
#         mean_temp REAL,
#         max_temp REAL,
#         min_temp REAL,
#         dominant_condition TEXT
#     )
#     ''')
#
#     # Insert data into the database
#     for date, row in daily_summary.iterrows():
#         cursor.execute('''
#         INSERT OR REPLACE INTO daily_weather_summary (date, mean_temp, max_temp, min_temp, dominant_condition)
#         VALUES (?, ?, ?, ?, ?)
#         ''', (date, row['current_temp']['mean'], row['current_temp']['max'], row['current_temp']['min'],
#               row['main_condition'][0]))
#
#     conn.commit()
#     conn.close()
#
#
# # Example usage:
# if __name__ == "__main__":
#     # Simulate fetching weather data
#     example_data = {
#         'main': {
#             'temp': 300.15,  # Example in Kelvin
#             'feels_like': 305.15
#         },
#         'weather': [{'main': 'Clear'}],
#         'dt': 1729223511  # Example timestamp
#     }
#
#     # Process multiple example data entries for a complete day
#     for i in range(5):  # Simulating 5 data entries for the same day
#         process_weather_data(example_data)
#
#     # Generate daily summary after processing data
#     generate_daily_summary()


# import pandas as pd
# import sqlite3
#
# # Global list to store weather data
# weather_data_storage = []
#
# def convert_kelvin_to_celsius(kelvin):
#     """Convert Kelvin to Celsius."""
#     return kelvin - 273.15
#
# def process_weather_data(data):
#     """Process the fetched weather data."""
#     main = data['main']
#     weather = data['weather'][0]
#
#     current_temp = convert_kelvin_to_celsius(main['temp'])
#     feels_like_temp = convert_kelvin_to_celsius(main['feels_like'])
#
#     # Append processed data to storage
#     weather_data_storage.append({
#         'main_condition': weather['main'],
#         'current_temp': current_temp,
#         'feels_like_temp': feels_like_temp,
#         'dt': data['dt']
#     })
#
# def generate_daily_summary():
#     """Generate daily summary from stored weather data."""
#     # Convert stored data to a DataFrame
#     df = pd.DataFrame(weather_data_storage)
#
#     if df.empty:
#         print("No weather data available for summary.")
#         return
#
#     # Convert 'dt' to datetime
#     df['dt'] = pd.to_datetime(df['dt'], unit='s')
#
#     # Daily aggregates
#     daily_summary = df.groupby(df['dt'].dt.date).agg({
#         'current_temp': ['mean', 'max', 'min'],
#         'main_condition': lambda x: x.mode()[0]  # Dominant condition
#     })
#
#     # Print the daily summary
#     print("Daily Weather Summary:")
#     for date, row in daily_summary.iterrows():
#         print(f"Date: {date}, Mean Temp: {row['current_temp']['mean']:.2f}°C, "
#               f"Max Temp: {row['current_temp']['max']:.2f}°C, "
#               f"Min Temp: {row['current_temp']['min']:.2f}°C, "
#               f"Dominant Condition: {row['main_condition'].iloc[0]}")  # Changed to .iloc[0]
#
#     # Store in a database
#     store_daily_summary(daily_summary)
#
# def store_daily_summary(daily_summary):
#     """Store daily summary in SQLite database."""
#     conn = sqlite3.connect('weather_summary.db')
#     cursor = conn.cursor()
#
#     # Create table if it doesn't exist
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS daily_weather_summary (
#         date DATE PRIMARY KEY,
#         mean_temp REAL,
#         max_temp REAL,
#         min_temp REAL,
#         dominant_condition TEXT
#     )
#     ''')
#
#     # Insert data into the database
#     for date, row in daily_summary.iterrows():
#         cursor.execute('''
#         INSERT OR REPLACE INTO daily_weather_summary (date, mean_temp, max_temp, min_temp, dominant_condition)
#         VALUES (?, ?, ?, ?, ?)
#         ''', (date, row['current_temp']['mean'], row['current_temp']['max'], row['current_temp']['min'],
#               row['main_condition'].iloc[0]))  # Changed to .iloc[0]
#
#     conn.commit()
#     conn.close()
#
# # Example usage:
# if __name__ == "__main__":
#     # Simulate fetching weather data
#     example_data = {
#         'main': {
#             'temp': 300.15,  # Example in Kelvin
#             'feels_like': 305.15
#         },
#         'weather': [{'main': 'Clear'}],
#         'dt': 1729223511  # Example timestamp
#     }
#
#     # Process multiple example data entries for a complete day
#     for i in range(5):  # Simulating 5 data entries for the same day
#         process_weather_data(example_data)
#
#     # Generate daily summary after processing data
#     generate_daily_summary()
# import pandas as pd
# import sqlite3
# import time
#
# #Global list to store weather data
# weather_data_storage = []
#
# def convert_kelvin_to_celsius(kelvin):
#     """Convert Kelvin to Celsius."""
#     return kelvin - 273.15
#
# def process_weather_data(data):
#     """Process the fetched weather data."""
#     main = data['main']
#     weather = data['weather'][0]
#
#     current_temp = convert_kelvin_to_celsius(main['temp'])
#     feels_like_temp = convert_kelvin_to_celsius(main['feels_like'])
#
#     # Check for invalid temperatures
#     if current_temp < -50:  # Arbitrary limit
#         print("Warning: Invalid temperature detected, skipping this entry.")
#         return
#
#     # Append processed data to storage
#     weather_data_storage.append({
#         'main_condition': weather['main'],
#         'current_temp': current_temp,
#         'feels_like_temp': feels_like_temp,
#         'dt': data['dt']
#     })
# def process_weather_data(data):
#     """Process the fetched weather data."""
#     if not data:
#         logging.warning("No data to process.")
#         return None
#
#     try:
#         city = data['name']
#         temperature = data['main']['temp']
#         humidity = data['main']['humidity']
#         condition = data['weather'][0]['main']
#
#         # Store the current temperature for summary calculations
#         weather_data_storage.append({
#             'city': city,
#             'temperature': temperature,
#             'humidity': humidity,
#             'condition': condition,
#             'timestamp': data['dt']
#         })
#
#         return {
#             'city': city,
#             'temperature': temperature,
#             'humidity': humidity,
#             'condition': condition
#         }
#     except KeyError as e:
#         logging.error(f"Key error: {e} - possibly the data format has changed.")
#         return None
#
#
# def generate_daily_summary():
#     """Generate daily summary from stored weather data."""
#     # Convert stored data to a DataFrame
#     df = pd.DataFrame(weather_data_storage)
#
#     if df.empty:
#         print("No weather data available for summary.")
#         return
#
#     # Convert 'dt' to datetime
#     df['dt'] = pd.to_datetime(df['dt'], unit='s')
#
#     # Daily aggregates
#     daily_summary = df.groupby(df['dt'].dt.date).agg({
#         'current_temp': ['mean', 'max', 'min'],
#         'main_condition': lambda x: x.mode()[0]  # Dominant condition
#     })
#
#     # Print the daily summary
#     print("Daily Weather Summary:")
#     for date, row in daily_summary.iterrows():
#         print(f"Date: {date}, Mean Temp: {row['current_temp']['mean']:.2f}°C, "
#               f"Max Temp: {row['current_temp']['max']:.2f}°C, "
#               f"Min Temp: {row['current_temp']['min']:.2f}°C, "
#               f"Dominant Condition: {row['main_condition']}")
#
# def store_daily_summary(daily_summary):
#     """Store daily summary in SQLite database."""
#     conn = sqlite3.connect('weather_summary.db')
#     cursor = conn.cursor()
#
#     # Create table if it doesn't exist
#     cursor.execute('''CREATE TABLE IF NOT EXISTS daily_weather_summary (
#         date DATE PRIMARY KEY,
#         mean_temp REAL,
#         max_temp REAL,
#         min_temp REAL,
#         dominant_condition TEXT
#     )''')
#
#     # Insert data into the database
#     for date, row in daily_summary.iterrows():
#         cursor.execute('''INSERT OR REPLACE INTO daily_weather_summary (date, mean_temp, max_temp, min_temp, dominant_condition)
#                           VALUES (?, ?, ?, ?, ?)''',
#                        (date, row['current_temp']['mean'], row['current_temp']['max'], row['current_temp']['min'],
#                         row['main_condition']))
#
#     conn.commit()
#     conn.close()
#
# # Example usage:
# if __name__ == "__main__":
#     # Simulate fetching weather data
#     example_data = {
#         'main': {
#             'temp': 300.15,  # Example in Kelvin
#             'feels_like': 305.15
#         },
#         'weather': [{'main': 'Clear'}],
#         'dt': int(time.time())  # Current Unix timestamp
#     }
#
#     # Process multiple example data entries for a complete day
#     for i in range(5):  # Simulating 5 data entries for the same day
#         process_weather_data(example_data)
#
#     # Generate daily summary after processing data
#     generate_daily_summary()


# import pandas as pd
# import sqlite3
# import time
#
# # Global list to store weather data
# weather_data_storage = []
#
#
# def process_weather_data(data):
#     """Process the fetched weather data."""
#     if not data:
#         logging.warning("No data to process.")
#         return
#
#     try:
#         city = data['name']
#         temperature = data['main']['temp']
#         condition = data['weather'][0]['main']
#         weather_data_storage.append({
#             'city': city,
#             'temperature': temperature,
#             'condition': condition,
#             'dt': data['dt']
#         })
#     except KeyError as e:
#         logging.error(f"Key error: {e} - possibly the data format has changed.")
#
#
# def generate_daily_summary():
#     """Generate daily summary from stored weather data."""
#     df = pd.DataFrame(weather_data_storage)
#
#     if df.empty:
#         print("No weather data available for summary.")
#         return pd.DataFrame()  # Return an empty DataFrame
#
#     # Convert 'dt' to datetime
#     df['dt'] = pd.to_datetime(df['dt'], unit='s')
#
#     # Daily aggregates
#     daily_summary = df.groupby(df['dt'].dt.date).agg({
#         'temperature': ['mean', 'max', 'min'],
#         'condition': lambda x: x.mode()[0]  # Dominant condition
#     })
#
#     # Flatten the MultiIndex columns
#     daily_summary.columns = ['mean_temp', 'max_temp', 'min_temp', 'dominant_condition']
#
#     # Print the daily summary
#     print("Daily Weather Summary:")
#     for date, row in daily_summary.iterrows():
#         print(f"Date: {date}, Mean Temp: {row['mean_temp']:.2f}°C, "
#               f"Max Temp: {row['max_temp']:.2f}°C, "
#               f"Min Temp: {row['min_temp']:.2f}°C, "
#               f"Dominant Condition: {row['dominant_condition']}")
#
#     return daily_summary  # Return the daily summary for further processing
#
#
# def store_daily_summary(daily_summary):
#     """Store daily summary in SQLite database."""
#     conn = sqlite3.connect('weather_summary.db')
#     cursor = conn.cursor()
#
#     # Create table if it doesn't exist
#     cursor.execute('''CREATE TABLE IF NOT EXISTS daily_weather_summary (
#         date DATE PRIMARY KEY,
#         mean_temp REAL,
#         max_temp REAL,
#         min_temp REAL,
#         dominant_condition TEXT
#     )''')
#
#     # Insert data into the database
#     for date, row in daily_summary.iterrows():
#         cursor.execute('''INSERT OR REPLACE INTO daily_weather_summary (date, mean_temp, max_temp, min_temp, dominant_condition)
#                           VALUES (?, ?, ?, ?, ?)''',
#                        (date, row['mean_temp'], row['max_temp'], row['min_temp'], row['dominant_condition']))
#
#     conn.commit()
#     conn.close()
#


#
# import pandas as pd
# import sqlite3
# import time
# import logging
#
# # Global list to store weather data
# weather_data_storage = []
#
# def convert_kelvin_to_celsius(kelvin):
#     """Convert Kelvin to Celsius."""
#     return kelvin - 273.15
#
# def process_weather_data(data):
#     """Process the fetched weather data."""
#     if not data:
#         logging.warning("No data to process.")
#         return None
#
#     try:
#         main = data['main']
#         weather = data['weather'][0]
#
#         current_temp = convert_kelvin_to_celsius(main['temp'])
#         feels_like_temp = convert_kelvin_to_celsius(main['feels_like'])
#
#         # Check for invalid temperatures
#         if current_temp < -50:  # Arbitrary limit
#             print("Warning: Invalid temperature detected, skipping this entry.")
#             return
#
#         # Append processed data to storage
#         weather_data_storage.append({
#             'main_condition': weather['main'],
#             'current_temp': current_temp,
#             'feels_like_temp': feels_like_temp,
#             'dt': data['dt']
#         })
#     except KeyError as e:
#         logging.error(f"Key error: {e} - possibly the data format has changed.")
#
# def generate_daily_summary():
#     """Generate daily summary from stored weather data."""
#     # Convert stored data to a DataFrame
#     df = pd.DataFrame(weather_data_storage)
#
#     if df.empty:
#         print("No weather data available for summary.")
#         return
#
#     # Convert 'dt' to datetime
#     df['dt'] = pd.to_datetime(df['dt'], unit='s')
#
#     # Daily aggregates
#     daily_summary = df.groupby(df['dt'].dt.date).agg({
#         'current_temp': ['mean', 'max', 'min'],
#         'main_condition': lambda x: x.mode()[0]  # Dominant condition
#     })
#
#     # Print the daily summary
#     print("Daily Weather Summary:")
#     for date, row in daily_summary.iterrows():
#         print(f"Date: {date}, Mean Temp: {row['current_temp']['mean']:.2f}°C, "
#               f"Max Temp: {row['current_temp']['max']:.2f}°C, "
#               f"Min Temp: {row['current_temp']['min']:.2f}°C, "
#               f"Dominant Condition: {row['main_condition']}")
#
#     return daily_summary  # Return the summary for storing
#
# def store_daily_summary(daily_summary):
#     """Store daily summary in SQLite database."""
#     conn = sqlite3.connect('weather_summary.db')
#     cursor = conn.cursor()
#
#     # Create table if it doesn't exist
#     cursor.execute('''CREATE TABLE IF NOT EXISTS daily_weather_summary (
#         date DATE PRIMARY KEY,
#         mean_temp REAL,
#         max_temp REAL,
#         min_temp REAL,
#         dominant_condition TEXT
#     )''')
#
#     # Insert data into the database
#     for date, row in daily_summary.iterrows():
#         cursor.execute('''INSERT OR REPLACE INTO daily_weather_summary (date, mean_temp, max_temp, min_temp, dominant_condition)
#                           VALUES (?, ?, ?, ?, ?)''',
#                        (date, row['current_temp']['mean'], row['current_temp']['max'], row['current_temp']['min'],
#                         row['main_condition']))
#
#     conn.commit()
#     conn.close()
#
# # Example usage:
# if __name__ == "__main__":
#     # Simulate fetching weather data
#     example_data = {
#         'main': {
#             'temp': 300.15,  # Example in Kelvin
#             'feels_like': 305.15
#         },
#         'weather': [{'main': 'Clear'}],
#         'dt': int(time.time())  # Current Unix timestamp
#     }
#
#     # Process multiple example data entries for a complete day
#     for i in range(5):  # Simulating 5 data entries for the same day
#         process_weather_data(example_data)
#
#     # Generate daily summary after processing data
#     daily_summary = generate_daily_summary()
#
#     # Store the daily summary in the database
#     if daily_summary is not None:
#         store_daily_summary(daily_summary)
#
# def generate_daily_summary():
#     """Generate daily summary from stored weather data."""
#     # Convert stored data to a DataFrame
#     df = pd.DataFrame(weather_data_storage)
#
#     if df.empty:
#         print("No weather data available for summary.")
#         return None
#
#     # Convert 'dt' to datetime
#     df['dt'] = pd.to_datetime(df['dt'], unit='s')
#
#     # Daily aggregates
#     daily_summary = df.groupby(df['dt'].dt.date).agg({
#         'current_temp': ['mean', 'max', 'min'],
#         'main_condition': lambda x: x.mode()[0]  # Dominant condition
#     })
#
#     # Print the daily summary
#     print("Daily Weather Summary:")
#     for date, row in daily_summary.iterrows():
#         print(f"Date: {date}, Mean Temp: {row['current_temp']['mean']:.2f}°C, "
#               f"Max Temp: {row['current_temp']['max']:.2f}°C, "
#               f"Min Temp: {row['current_temp']['min']:.2f}°C, "
#               f"Dominant Condition: {row['main_condition']}")
#
#     return daily_summary.reset_index()  # Reset index for easier access
#
# def store_daily_summary(daily_summary):
#     """Store daily summary in SQLite database."""
#     conn = sqlite3.connect('weather_summary.db')
#     cursor = conn.cursor()
#
#     # Create table if it doesn't exist
#     cursor.execute('''CREATE TABLE IF NOT EXISTS daily_weather_summary (
#         date DATE PRIMARY KEY,
#         mean_temp REAL,
#         max_temp REAL,
#         min_temp REAL,
#         dominant_condition TEXT
#     )''')
#
#     # Insert data into the database
#     for _, row in daily_summary.iterrows():  # Iterate through the rows
#         cursor.execute('''INSERT OR REPLACE INTO daily_weather_summary (date, mean_temp, max_temp, min_temp, dominant_condition)
#                           VALUES (?, ?, ?, ?, ?)''',
#                        (row['dt'].date(),  # Access the date correctly
#                         row['current_temp']['mean'],
#                         row['current_temp']['max'],
#                         row['current_temp']['min'],
#                         row['main_condition']))  # Use the correct key
#
#     conn.commit()
#     conn.close()





import pandas as pd
import sqlite3
import time

# Global list to store weather data
weather_data_storage = []

def convert_kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def process_weather_data(data):
    """Process the fetched weather data."""
    main = data['main']
    weather = data['weather'][0]

    current_temp = convert_kelvin_to_celsius(main['temp'])
    feels_like_temp = convert_kelvin_to_celsius(main['feels_like'])

    # Check for invalid temperatures
    if current_temp < -50:  # Arbitrary limit
        print("Warning: Invalid temperature detected, skipping this entry.")
        return

    # Append processed data to storage
    weather_data_storage.append({
        'main_condition': weather['main'],
        'current_temp': current_temp,
        'feels_like_temp': feels_like_temp,
        'dt': data['dt']
    })

def generate_daily_summary():
    """Generate daily summary from stored weather data."""
    # Convert stored data to a DataFrame
    df = pd.DataFrame(weather_data_storage)

    if df.empty:
        print("No weather data available for summary.")
        return None

    # Convert 'dt' to datetime
    df['dt'] = pd.to_datetime(df['dt'], unit='s')

    # Daily aggregates
    daily_summary = df.groupby(df['dt'].dt.date).agg({
        'current_temp': ['mean', 'max', 'min'],
        'main_condition': lambda x: x.mode()[0] if not x.mode().empty else 'Unknown'  # Dominant condition
    })

    # Print the daily summary
    print("Daily Weather Summary:")
    for date, row in daily_summary.iterrows():
        print(f"Date: {date}, Mean Temp: {row['current_temp']['mean']:.2f}°C, "
              f"Max Temp: {row['current_temp']['max']:.2f}°C, "
              f"Min Temp: {row['current_temp']['min']:.2f}°C, "
              f"Dominant Condition: {row['main_condition']}")

    return daily_summary.reset_index()  # Reset index for easier access



def store_daily_summary(daily_summary):
    """Store daily summary in SQLite database."""
    conn = sqlite3.connect('weather_summary.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS daily_weather_summary (
        date DATE PRIMARY KEY,
        mean_temp REAL,
        max_temp REAL,
        min_temp REAL,
        dominant_condition TEXT
    )''')

    # Insert data into the database
    for date, row in daily_summary.iterrows():
        cursor.execute('''INSERT OR REPLACE INTO daily_weather_summary (date, mean_temp, max_temp, min_temp, dominant_condition)
                          VALUES (?, ?, ?, ?, ?)''',
                       (date, row['current_temp']['mean'], row['current_temp']['max'], row['current_temp']['min'],
                        row['main_condition']))  # Fix this line

    conn.commit()
    conn.close()


# Example usage:
if __name__ == "__main__":
    # Simulate fetching weather data
    example_data = {
        'main': {
            'temp': 300.15,  # Example in Kelvin
            'feels_like': 305.15
        },
        'weather': [{'main': 'Clear'}],
        'dt': int(time.time())  # Current Unix timestamp
    }

    # Process multiple example data entries for a complete day
    for i in range(5):  # Simulating 5 data entries for the same day
        process_weather_data(example_data)

    # Generate daily summary after processing data
    daily_summary = generate_daily_summary()

    # Store daily summary in the database
    if daily_summary is not None:
        store_daily_summary(daily_summary)



#  it is printing all the data saved in the daatbse import pandas as pd
# import sqlite3
# import time
#
# # Global list to store weather data
# weather_data_storage = []
#
# def convert_kelvin_to_celsius(kelvin):
#     """Convert Kelvin to Celsius."""
#     return kelvin - 273.15
#
# def process_weather_data(data):
#     """Process the fetched weather data."""
#     main = data['main']
#     weather = data['weather'][0]
#
#     current_temp = convert_kelvin_to_celsius(main['temp'])
#     feels_like_temp = convert_kelvin_to_celsius(main['feels_like'])
#
#     # Check for invalid temperatures
#     if current_temp < -50:  # Arbitrary limit
#         print("Warning: Invalid temperature detected, skipping this entry.")
#         return
#
#     # Append processed data to storage
#     weather_data_storage.append({
#         'main_condition': weather['main'],
#         'current_temp': current_temp,
#         'feels_like_temp': feels_like_temp,
#         'dt': data['dt']
#     })
#
# def generate_daily_summary():
#     """Generate daily summary from stored weather data."""
#     # Convert stored data to a DataFrame
#     df = pd.DataFrame(weather_data_storage)
#
#     if df.empty:
#         print("No weather data available for summary.")
#         return None
#
#     # Convert 'dt' to datetime
#     df['dt'] = pd.to_datetime(df['dt'], unit='s')
#
#     # Daily aggregates
#     daily_summary = df.groupby(df['dt'].dt.date).agg({
#         'current_temp': ['mean', 'max', 'min'],
#         'main_condition': lambda x: x.mode()[0] if not x.mode().empty else 'Unknown'  # Dominant condition
#     })
#
#     # Print the daily summary
#     print("Daily Weather Summary:")
#     for date, row in daily_summary.iterrows():
#         print(f"Date: {date}, Mean Temp: {row['current_temp']['mean']:.2f}°C, "
#               f"Max Temp: {row['current_temp']['max']:.2f}°C, "
#               f"Min Temp: {row['current_temp']['min']:.2f}°C, "
#               f"Dominant Condition: {row['main_condition']}")
#
#     return daily_summary.reset_index()  # Reset index for easier access
#
# def store_daily_summary(daily_summary):
#     """Store daily summary in SQLite database."""
#     conn = sqlite3.connect('weather_summary.db')
#     cursor = conn.cursor()
#
#     # Create table if it doesn't exist
#     cursor.execute('''CREATE TABLE IF NOT EXISTS daily_weather_summary (
#         date DATE PRIMARY KEY,
#         mean_temp REAL,
#         max_temp REAL,
#         min_temp REAL,
#         dominant_condition TEXT
#     )''')
#
#     # Insert data into the database
#     for date, row in daily_summary.iterrows():  # Iterate through the rows
#         cursor.execute('''INSERT OR REPLACE INTO daily_weather_summary (date, mean_temp, max_temp, min_temp, dominant_condition)
#                           VALUES (?, ?, ?, ?, ?)''',
#                        (date,  # Use the date directly
#                         row['current_temp']['mean'],
#                         row['current_temp']['max'],
#                         row['current_temp']['min'],
#                         row['main_condition']))  # Use the correct key
#
#     conn.commit()
#     conn.close()
#
# # Example usage:
# if __name__ == "__main__":
#     # Simulate fetching weather data
#     example_data = {
#         'main': {
#             'temp': 300.15,  # Example in Kelvin
#             'feels_like': 305.15
#         },
#         'weather': [{'main': 'Clear'}],
#         'dt': int(time.time())  # Current Unix timestamp
#     }
#
#     # Process multiple example data entries for a complete day
#     for i in range(5):  # Simulating 5 data entries for the same day
#         process_weather_data(example_data)
#
#     # Generate daily summary after processing data
#     daily_summary = generate_daily_summary()
#
#     # Store daily summary in the database
#     if daily_summary is not None:
#         store_daily_summary(daily_summary)
#
