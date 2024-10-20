# import matplotlib.pyplot as plt
# def plot_weather_summary(weather):
#     # Example plotting function
#     weather.plot(x='date', y='avg_temp', kind='bar')
#     plt.title('Daily Average Temperatures')
#     plt.show()



# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Example weather data
# data = {
#     'date': ['2024-10-14', '2024-10-15', '2024-10-16', '2024-10-17'],
#     'avg_temp': [28, 30, 27, 29]
# }
# weather_df = pd.DataFrame(data)
#
# def plot_weather_summary(weather):
#     # Example plotting function
#     weather.plot(x='date', y='avg_temp', kind='bar')
#     plt.title('Daily Average Temperatures')
#     plt.xlabel('Date')
#     plt.ylabel('Average Temperature (°C)')
#     plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
#     plt.tight_layout()  # Adjust layout to make room for labels
#     plt.show()
#
# # Call the function to plot the summary
# plot_weather_summary(weather_df)



import pandas as pd
import matplotlib.pyplot as plt

# Sample data for daily summaries
daily_summary_data = {
    'date': ['2024-10-14', '2024-10-15', '2024-10-16', '2024-10-17'],
    'avg_temp': [28, 30, 27, 29],
    'avg_humidity': [60, 65, 58, 62],
    'alerts': [0, 1, 0, 0]  # 1 indicates an alert was triggered
}
daily_summary_df = pd.DataFrame(daily_summary_data)

# Sample historical trends data
historical_trends_data = {
    'date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'avg_temp': [25, 26, 24, 27, 28, 29, 30, 31, 29, 28]
}
historical_trends_df = pd.DataFrame(historical_trends_data)

# Sample alerts data
alerts_data = {
    'date': ['2024-10-15'],
    'alert_type': ['High Temperature'],
    'details': ['Temperature exceeded 30°C']
}
alerts_df = pd.DataFrame(alerts_data)

# Function to visualize daily weather summaries
def plot_daily_summary(summary_df):
    summary_df.plot(x='date', y=['avg_temp', 'avg_humidity'], kind='bar')
    plt.title('Daily Weather Summaries')
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.xticks(rotation=45)
    plt.legend(['Average Temperature (°C)', 'Average Humidity (%)'])
    plt.tight_layout()
    plt.show()

# Function to visualize historical trends
def plot_historical_trends(trends_df):
    plt.plot(trends_df['date'], trends_df['avg_temp'], marker='o')
    plt.title('Historical Temperature Trends')
    plt.xlabel('Date')
    plt.ylabel('Average Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()

# Function to visualize triggered alerts
def plot_triggered_alerts(alerts_df):
    if not alerts_df.empty:
        plt.figure(figsize=(8, 4))
        plt.bar(alerts_df['date'], alerts_df['alert_type'], color='red')
        plt.title('Triggered Alerts')
        plt.xlabel('Date')
        plt.ylabel('Alert Type')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("No alerts triggered.")

# Run visualizations
plot_daily_summary(daily_summary_df)
plot_historical_trends(historical_trends_df)
plot_triggered_alerts(alerts_df)

# Test Cases
def test_system_setup():
    assert not daily_summary_df.empty, "Daily Summary DataFrame is empty."
    assert 'date' in daily_summary_df.columns, "Date column missing in daily summary."
    assert 'avg_temp' in daily_summary_df.columns, "Average Temperature column missing."
    assert 'avg_humidity' in daily_summary_df.columns, "Average Humidity column missing."
    print("System Setup: Daily Summary DataFrame is configured correctly.")

def test_alerts():
    assert 'alert_type' in alerts_df.columns, "Alert Type column missing in alerts."
    print("Alerts Test: Alert Type column is present.")

# Run tests
test_system_setup()
test_alerts()

