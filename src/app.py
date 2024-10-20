# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     daily_summary = {
#         'date': '2024-10-17',
#         'avg_temp': 28,
#         'max_temp': 30,
#         'min_temp': 25,
#         'dominant_condition': 'Clear'
#     }
#     return render_template('index.html', summary=daily_summary)
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
# from flask import Flask, render_template, jsonify
# import sqlite3
#
# app = Flask(__name__)
#
# DB_NAME = 'weather_data.db'
#
# def get_latest_weather():
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()
#     cursor.execute('SELECT city, temperature, humidity, condition, timestamp FROM weather ORDER BY timestamp DESC LIMIT 1')
#     result = cursor.fetchone()
#     conn.close()
#     return result
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/data')
# def data():
#     latest_weather = get_latest_weather()
#     if latest_weather:
#         city, temperature, humidity, condition, timestamp = latest_weather
#         return jsonify({
#             'city': city,
#             'temperature': temperature,
#             'humidity': humidity,
#             'condition': condition,
#             'timestamp': timestamp
#         })
#     return jsonify({'error': 'No data available'})
#
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, jsonify
# import sqlite3
# import pandas as pd
#
# app = Flask(__name__)
#
# def get_weather_summary():
#     """Fetch daily weather summary from the SQLite database."""
#     conn = sqlite3.connect('weather_summary.db')
#     query = "SELECT date, mean_temp, max_temp, min_temp, dominant_condition FROM daily_weather_summary"
#     df = pd.read_sql(query, conn)
#     conn.close()
#     return df
#
# # @app.route('/')
# # def index():
# #     """Render the main page."""
# #     return render_template('index.html')
#
# @app.route('/')
# def index():
#     """Render the main page with weather data."""
#     summary = get_weather_summary()
#     return render_template('index.html', weather_data=summary.to_dict(orient='records'))
#
#
# @app.route('/data')
# def data():
#     """Fetch and return weather data as JSON."""
#     summary = get_weather_summary()
#     return jsonify(summary.to_dict(orient='records'))
#
# if __name__ == "__main__":
#     app.run(debug=True)
#
#


# from flask import Flask, render_template, jsonify
# import sqlite3
# import pandas as pd
#
# app = Flask(__name__)
#
# def get_weather_summary():
#     """Fetch daily weather summary from the SQLite database."""
#     conn = sqlite3.connect('weather_summary.db')
#     query = "SELECT * FROM daily_weather_summary"
#     df = pd.read_sql(query, conn)
#     conn.close()
#     return df
#
# @app.route('/')
# def index():
#     """Render the main page."""
#     return render_template('index.html')
#
# @app.route('/data')
# def data():
#     """Fetch and return weather data as JSON."""
#     summary = get_weather_summary()
#     return jsonify(summary.to_dict(orient='records'))
#
# if __name__ == "__main__":
#     app.run(debug=True)
#
#


# from flask import Flask, render_template, jsonify
# import sqlite3
# app = Flask(__name__)
#
# DB_NAME = 'weather_data.db'
#
# def get_latest_weather():
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()
#     cursor.execute('SELECT city, temperature, humidity, condition, timestamp FROM weather ORDER BY timestamp DESC LIMIT 1')
#     result = cursor.fetchone()
#     conn.close()
#     return result
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/data')
# def data():
#     latest_weather = get_latest_weather()
#     if latest_weather:
#         city, temperature, humidity, condition, timestamp = latest_weather
#         return jsonify({
#             'city': city,
#             'temperature': temperature,
#             'humidity': humidity,
#             'condition': condition,
#             'timestamp': timestamp
#         })
#     return jsonify({'error': 'No data available'})
#
# if __name__ == '__main__':
#     app.run(debug=True)

#  from flask import Flask, render_template, jsonify
# from flask_sqlalchemy import SQLAlchemy
# import requests
#
# app = Flask(__name__)
# #
# # # Configure the SQLite database
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather_data.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # db = SQLAlchemy(app)
# #
# #
# # # Define your database model
# # class Weather(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     city = db.Column(db.String(50), nullable=False)
# #     temperature = db.Column(db.Float, nullable=False)
# #     humidity = db.Column(db.Float, nullable=False)
# #     condition = db.Column(db.String(50), nullable=False)
# #
# #
# # # Fetch weather data from OpenWeatherMap
# # API_KEY = 'your_api_key_here'  # Replace with your actual API key
# #
# #
# # def get_weather_data(city):
# #     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
# #     response = requests.get(url)
# #     return response.json()
# #
# #
# # @app.route('/')
# # def index():
# #     return render_template('index.html')
# #
# #
# # @app.route('/data')
# # def data():
# #     city = 'Delhi'  # Change this to the city you want
# #     weather_data = get_weather_data(city)
# #     if weather_data.get('cod') == 200:
# #         city = weather_data['name']
# #         temperature = weather_data['main']['temp']
# #         humidity = weather_data['main']['humidity']
# #         condition = weather_data['weather'][0]['main']
# #
# #         # Save to the database
# #         new_weather = Weather(city=city, temperature=temperature, humidity=humidity, condition=condition)
# #         db.session.add(new_weather)
# #         db.session.commit()
# #
# #         return jsonify({'city': city, 'temperature': temperature, 'humidity': humidity, 'condition': condition})
# #     return jsonify({'error': 'City not found'}), 404
# #
# #
# # if __name__ == '__main__':
# #     with app.app_context():  # Create application context
# #         db.create_all()  # Create the database tables
# #     app.run(debug=True)
# #
# #

# from flask import Flask, render_template, jsonify, request
# import sqlite3
#
# app = Flask(__name__)
#
# DB_NAME = 'weather_data.db'
#
# def get_weather_summary(city):
#     """Fetch daily weather summary for a specific city from the SQLite database."""
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()
#     query = """
#         SELECT date, mean_temp, max_temp, min_temp, dominant_condition
#         FROM daily_weather_summary
#         WHERE city = ?
#         ORDER BY date DESC LIMIT 1
#     """
#     cursor.execute(query, (city,))
#     result = cursor.fetchone()
#     conn.close()
#     return result
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/data', methods=['POST'])
# def data():
#     city = request.json.get('city')
#     weather_summary = get_weather_summary(city)
#     if weather_summary:
#         date, mean_temp, max_temp, min_temp, dominant_condition = weather_summary
#         return jsonify({
#             'date': date,
#             'mean_temp': mean_temp,
#             'max_temp': max_temp,
#             'min_temp': min_temp,
#             'dominant_condition': dominant_condition
#         })
#     return jsonify({'error': 'No data available for the city selected'})
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

DB_NAME = 'weather_summary.db'

def get_weather_summary():
    """Fetch daily weather summary from the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    query = "SELECT date, mean_temp, max_temp, min_temp, dominant_condition FROM daily_weather_summary"
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()  # Fetch all results
    conn.close()
    return results


@app.route('/')
def index():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM weather ORDER BY timestamp DESC')
    weather_rows = cursor.fetchall()

    # Fetch daily summary
    cursor.execute('SELECT * FROM daily_weather_summary ORDER BY date DESC')
    daily_summary_rows = cursor.fetchall()
    conn.close()

    return render_template('index.html', weather_data=weather_rows, daily_summary=daily_summary_rows)

# @app.route('/')
# def index():
#     """Render the main page with weather data."""
#     summary = get_weather_summary()
#     return render_template('index.html', weather_data=summary)

@app.route('/data', methods=['POST'])
def data():
    """Fetch and return weather data as JSON."""
    summary = get_weather_summary()
    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True)

