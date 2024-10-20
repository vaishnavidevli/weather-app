import time
import smtplib
from email.mime.text import MIMEText

# User-configurable thresholds
TEMPERATURE_THRESHOLD = 35  # Celsius
CONSECUTIVE_ALERTS = 2  # Number of consecutive updates to trigger alert
ALERT_CONDITIONS = ['Rainy', 'Stormy']  # Conditions to trigger alert

# Variables to track temperature alerts
alert_count = 0
last_temp = None


# Function to send email notifications
def send_email_alert(subject, message):
    # Email configuration (example using Gmail)
    sender = 'your_email@gmail.com'
    receiver = 'recipient_email@example.com'
    password = 'your_email_password'  # Use app password or a secure method

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    # Send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())


# Function to check weather data
def check_weather_conditions(weather_data):
    global alert_count, last_temp

    # Example weather data format
    # weather_data = {'temperature': 30, 'condition': 'Clear'}
    temperature = weather_data['temperature']
    condition = weather_data['condition']

    # Check temperature threshold
    if temperature > TEMPERATURE_THRESHOLD:
        alert_count += 1
        if alert_count >= CONSECUTIVE_ALERTS:
            alert_message = f"Alert! Temperature has exceeded {TEMPERATURE_THRESHOLD}°C for {CONSECUTIVE_ALERTS} consecutive updates. Current temperature: {temperature}°C."
            print(alert_message)
            send_email_alert("Temperature Alert", alert_message)
    else:
        alert_count = 0  # Reset alert count if temperature is within the limit

    # Check weather condition
    if condition in ALERT_CONDITIONS:
        alert_message = f"Alert! Current weather condition is {condition}."
        print(alert_message)
        send_email_alert("Weather Condition Alert", alert_message)


# Main loop to simulate continuous tracking
if __name__ == "__main__":
    while True:
        # Simulate getting real-time weather data
        # Replace this with your actual data retrieval method
        # Example: weather_data = get_weather_data()
        weather_data = {
            'temperature': 36,  # Simulated temperature
            'condition': 'Clear'  # Simulated condition
        }

        # Check the weather conditions
        check_weather_conditions(weather_data)

        # Sleep for a defined interval before checking again (e.g., every 5 minutes)
        time.sleep(300)  # Check every 5 minutes
