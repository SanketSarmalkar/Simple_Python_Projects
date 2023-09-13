import requests
import json
import win32com.client as wincom
import time

city = str(input("Enter the name of the city: "))
speak = wincom.Dispatch("SAPI.SpVoice")

url = f"http://api.weatherapi.com/v1/current.json?key=a7b3d88f7fda4f44a5e52452230904&q={city}"

response = requests.get(url)
# print(response.text)
# print(type(response.text)) string
final_sol = json.loads(response.text)
temperature = final_sol["current"]["temp_c"]
hear = f"The temperature of {city} is {str(temperature)} degree celsius"
# hear = "Python text-to-speech test. using win32com.client"
speak.Speak(hear)
