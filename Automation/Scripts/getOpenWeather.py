#! python3
# getOpenWeather.py - Prints the weather for a location
# from the command line

APPID = 'd7216ae27df7e86a851e1658edc8a2ee'

import json, requests, sys

# Computer location from comand line arguments

if len(sys.argv) < 2 :
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])
# OpenWeatherMap.org provides real-time weather information
# in JSON format
# Download the JSON data from OpenWeatherMap.org's API. 

url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location,APPID)

response = requests.get(url)
response.raise_for_status()
# Uncomment to see the raw JSON text: 
# print(response.text)
# Load JSON data into python variable
weatherData = json.loads(response.text)
# Print weather descriptions
w = weatherData['weather']
print('Current Weather in %s:' % (location))
print(w[0]['main'],w[0]['description'])

