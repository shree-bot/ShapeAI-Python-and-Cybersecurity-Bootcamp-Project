
'''This is a python program that fetch the weather report of the requested area and
prints it in the terminal and also saves the data in a text file named weather_text_file.txt'''
import requests

from datetime import datetime

api_key = 'b4794a3fe3c87740e3cc9695fc1095c9'


location = input("Enter the city name:")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid=" + api_key

api_link = requests.get(complete_api_link)
api_data = api_link.json()

# create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
humidity = api_data['main']['humidity']
Wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-----------------------------------------------------")
print("Weather Stats for - {} || {}".format(location.upper(), date_time))
print("-----------------------------------------------------")

print("Current temperature is : {:.2f} deg C".format(temp_city))
print("Current weather desc :", weather_desc)
print("current Humidity     :", humidity, '%')
print("Current wind speed   :", Wind_spd, 'kmph')

text_file = open("weather_text_file.txt", "a+")
text_file.write("\ntemperature:" + str(temp_city))
text_file.write("\nweather_dec:" + str(weather_desc))
text_file.write("\nHumidity:" + str(humidity))
text_file.write("\nwind_spd:" + str(Wind_spd))
text_file.write("\ndate_time:" + str(date_time))
text_file.write("\n")
text_file.close()
text_file = open("weather_text_file.txt", "r")
print("\ndata from text file\n")
print(text_file.read())
print()
text_file.close()