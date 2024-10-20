#test_weather.py
import pytest
# src/__init__.py
from src.weather_api import fetch_weather_data

# Adjust the import path as necessary


def test_fetch_weather_data_valid():
    api_key = 'e52aef32f94d9748d6e861d1b1a6cc44'  # Replace with a valid API key
    location = 'Delhi'
    weather_data = fetch_weather_data(location, api_key)

    assert weather_data is not None
    assert 'weather' in weather_data
    assert 'main' in weather_data


def test_fetch_weather_data_invalid():
    api_key = 'invalid_api_key'  # Use an invalid API key to test error handling
    location = 'Delhi'
    weather_data = fetch_weather_data(location, api_key)

    assert weather_data is None  # Expect None for invalid API key
