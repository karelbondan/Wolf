import os
import random
from configparser import ConfigParser
import playsound
import requests
from gtts import gTTS

# opening the config.ini which has the API key in it for the openweather API.
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

# opening the city database list for further checking.
# this city database was made by anuveyatsu. Their github repo link is https://github.com/datasets/world-cities
with open("cities.csv", 'r', encoding='utf8') as f:
    file = f.read()
data = file.split('\n')
cities_list = []  # this list is where the cities are going to be stored.
for i in range(len(data) - 1):
    city = data[i][:data[i].find(',')].lower()
    cities_list.append(city)


# for the assistant to be able to give a respond
def voice_output_weather(answer):
    audiocreated = gTTS(text=answer, lang='en', slow=False)
    a = random.randint(1, 999)
    audiocreated.save(f'tts_temp-{a}.mp3')
    playsound.playsound(f'tts_temp-{a}.mp3')
    os.remove(f'tts_temp-{a}.mp3')
    return answer


# --- the main functions ---
# function that calls the API and searches for the current weather for the city.
# the default city is Jakarta in case the user doesn't specify a city.
def weather(city):
    cur_city = city[1]
    res = requests.get(url=f'https://api.openweathermap.org/data/2.5/weather?q={cur_city}&appid={api_key}')
    if res:
        file = res.json()
        city = file['name']
        country = file['sys']['country']
        temp = file['main']['temp']
        temp_celcius = int(round(temp - 273.15, 0))
        temp_fahrenheit = int(round((temp - 273.15) * 9 / 5 + 32, 0))
        icon = file['weather'][0]['icon']
        weather = file['weather'][0]['main']
        pressure = str(file['main']['pressure'])
        humidity = str(file['main']['humidity'])
        visibility = str(file['visibility'])
        feels_like = file['main']['feels_like']
        feels_like = int(round(feels_like - 273.15, 0))
        description = file['weather'][0]['description']
        append_all = [city, country, temp_celcius, temp_fahrenheit, icon, weather, humidity, visibility, pressure,
                      feels_like, description]
    else:
        return None
    return append_all


# checking the user input. If counter > 3 then it will recognize that the user is trying to ask what is the
# current weather of the city, else it will pass the statement and instead go to google or any search engine
# the user has specified for further search.
def check_userinput(usrinput):
    usrinput = usrinput.split()
    counter = 0
    this_city = ''
    weather_check_input = ['how', 'weather', 'today', 'what', 'current', 'of', 'now']
    for items in usrinput:
        if items in weather_check_input:
            counter += 1
        elif items in cities_list:
            this_city += items
            counter += 1
        else:
            pass
    if this_city == '':
        this_city = 'jakarta'
    else:
        pass
    return counter, this_city
