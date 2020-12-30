import datetime
from gtts import gTTS
import os
import random
import playsound
import time
import string

# dictionary containing the list of things used for later
dict_days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
             5: 'Friday', 6: 'Saturday', 7: 'Sunday '}
dict_months = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': "June",
               '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
time_12hr = {'13': '01', '14': '02', '15': '03', '16': '04', '17': '05', '18': '06', '19': '07',
             '20': '08', '21': '09', '22': '10', '23': '11', '00': '12'}


# voice assistant
def voice_output_time(answer):
    audiocreated = gTTS(text=answer, lang='en', slow=False)
    a = random.randint(1, 999)
    audiocreated.save(f'tts_temp-{a}.mp3')
    playsound.playsound(f'tts_temp-{a}.mp3')
    os.remove(f'tts_temp-{a}.mp3')
    return answer


# to show the current time
def day_now():
    day_today = str(datetime.date.today()).split('-')
    time_now = time.ctime().split()
    final_time_now = ''

    if time_now[-2][:2] in time_12hr.keys():
        final_time_now += f'{time_12hr[time_now[-2][:2]]}{time_now[-2][2:5]} PM'
    elif time_now[-2][:2] == '00':
        final_time_now += f'{time_12hr[time_now[-2][:2]]}{time_now[-2][2:5]} AM'
    elif time_now[-2][:2] == '12':
        final_time_now += f'{time_now[-2][:2]}{time_now[-2][2:5]} PM'
    else:
        final_time_now += f'{time_now[-2][:2]}{time_now[-2][2:5]} AM'

    day = datetime.datetime.now().isoweekday()  # to determine the current day of the week

    final_format = f'Today is {dict_days[day]}, {day_today[2]} {dict_months[day_today[1]]} {day_today[0]}, {time_now[-2][:5]}'
    asis_format = f'Today is {dict_days[day]}, {day_today[2]} {dict_months[day_today[1]]} {day_today[0]}, {final_time_now}'
    return final_format, asis_format


# checking the user input. If counter > 3 then it will recognize that the user is trying to ask what is the
# current weather of the city, else it will pass the statement and instead go to google or any search engine
# the user has specified for further search.
def check_userinput(usrinput):
    day = datetime.datetime.now().isoweekday()  # to determine the current day of the week
    if 'what day is tomorrow' in usrinput:
        if day + 1 == 8:
            day = 1
            tomorrow = f'tomorrow is {dict_days[day]}'
            print(tomorrow)
            return tomorrow
        else:
            tomorrow = f'tomorrow is {dict_days[day]}'
            print(tomorrow)
            return tomorrow
    elif 'what day is yesterday' in usrinput:
        if day - 1 == 0:
            day = 7
            yesterday = f'yesterday is {dict_days[day]}'
            print(yesterday)
            return yesterday
        else:
            yesterday = f'yesterday is {dict_days[day - 1]}'
            print(yesterday)
            return yesterday
    usrinput = usrinput.split()
    counter = 0
    time_check_input = ['current', 'time', 'now', 'today', 'what', 'it', 'year']
    for items in usrinput:
        if items in time_check_input:
            counter += 1
        else:
            pass
    print(counter)
    return counter


"""
usrinput = 'what day is it today'
input_check = check_userinput(usrinput)
if type(input_check) == str:
    voice_asis = voice_output_time(input_check)
else:
    if input_check >= 2:
        time = day_now()
        print(time[0])
        voice_asis = voice_output_time(time[1])
    else: pass
# """
