# import requests

# api_key = '4542341c0498bbc020c321bdc6b07acb'

# user_input = input("Enter City :")
# print( user_input)

# weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&unit=imperial&APPID={api_key}")

# print (weather_data.status_code)
# print(weather_data.json())

# weather = weather_data.json()['weather'][0]['main']
# temp = round(weather_data.json()['main']['temp'])

# print(f"The weather in {user_input} is: {weather}")
# print(f"The temperature in {user_input} is: {temp} F")


# https://api.openweathermap.org/data/2.5/weather?q=Cape Town&appid=4542341c0498bbc020c321bdc6b07acb