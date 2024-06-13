# from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS
# import requests
# import time

# app = Flask(__name__)
# CORS(app)

# @app.route('/')
# @app.route('/home')
# def home():
#     return render_template('index.html')

# @app.route('/getWeather', methods=['POST'])
# def getWeather():
#     data = request.get_json()
#     city = data['city']
#     # Get coordinates for the city
#     geocode_api = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid=4542341c0498bbc020c321bdc6b07acb"
#     geo_data = requests.get(geocode_api).json()
    
#     if not geo_data:
#         return jsonify({"error": "City not found"})
    
#     lat = geo_data[0]['lat']
#     lon = geo_data[0]['lon']
    
#     # Get 7-day weather forecast
#     api = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&appid=4542341c0498bbc020c321bdc6b07acb"
#     json_data = requests.get(api).json()
    
#     forecast = []
#     for day in json_data['daily']:
#         day_forecast = {
#             "date": time.strftime("%Y-%m-%d", time.gmtime(day['dt'])),
#             "condition": day['weather'][0]['main'],
#             "temp": int(day['temp']['day'] - 273.15),
#             "min_temp": int(day['temp']['min'] - 273.15),
#             "max_temp": int(day['temp']['max'] - 273.15),
#             "pressure": day['pressure'],
#             "humidity": day['humidity'],
#             "wind": day['wind_speed'],
#             "sunrise": time.strftime("%H:%M:%S", time.gmtime(day['sunrise'])),
#             "sunset": time.strftime("%H:%M:%S", time.gmtime(day['sunset']))
#         }
#         forecast.append(day_forecast)
    
#     return jsonify(forecast)

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/getWeather', methods=['POST'])
def getWeather():
    data = request.get_json()
    city = data['city']
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=4542341c0498bbc020c321bdc6b07acb"
    json_data = requests.get(api).json()
    
    if json_data.get('cod') != 200:
        return jsonify({"error": "City not found"})
    
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] + 7200))
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] + 7200))

    weather_info = {
        "condition": condition,
        "temp": temp,
        "min_temp": min_temp,
        "max_temp": max_temp,
        "pressure": pressure,
        "humidity": humidity,
        "wind": wind,
        "sunrise": sunrise,
        "sunset": sunset
    }

    return jsonify(weather_info)

if __name__ == '__main__':
    app.run(debug=True)


