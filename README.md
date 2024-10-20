
# weather-app
=======
## Project Overview
youtube link - : https://youtu.be/ZAySw2ONELg?si=KBI5iYC5PTNZFEHQ 

This project aims to develop a real-time data processing system for monitoring weather conditions using data retrieved from the OpenWeatherMap API. The system provides summarized insights through rollups and aggregates, including daily weather summaries and alerting for specified weather conditions.

## Objectives

- Continuously retrieve weather data for major Indian metros (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).
- Calculate daily weather summaries with averages, maximums, minimums, and dominant weather conditions.
- Implement a user-configurable alerting system based on temperature thresholds and specific weather conditions.
- Provide visualizations for daily summaries and historical trends.

## Data Source

The weather data is sourced from the [OpenWeatherMap API](https://openweathermap.org/). You will need to sign up for a free API key to access the data. The API provides various weather parameters, including:
- Main weather condition (e.g., Rain, Snow, Clear)
- Current temperature in Celsius
- Perceived temperature in Celsius
- Timestamp of the data update (Unix timestamp)

## Installation

### Prerequisites
- Python 3.6 or higher
- Required packages listed in `requirements.txt`

### Steps
1. Clone this repository:
   git clone https://github.com/PRANJALIMALETHA/Real-Time-Data-Processing-System-.git

Install dependencies:


2.pip install -r requirements.txt
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Set up a .env file


OPENWEATHER_API_KEY=your_api_key

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Run the main application script:

python src/main.py

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Run app.py
Running on http://127.0.0.1:5000
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To run the tests, you can use the following command
pytest tests/



   
>>>>>>> ca14682 (all files)
>>>>>>> 3316791 (all files)
