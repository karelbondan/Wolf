import wolframalpha

import apps
import checking as num
import webbrowser
import requests
from bs4 import BeautifulSoup
import re
from gtts import gTTS
import playsound
import os
import weather as wt
import string
import random
import jokes as jk
import day
import time
import youtube
import socket
import speech_recognition
import notes
import threading

sr = speech_recognition.Recognizer()

user_config = {}
destination_path = f'C:\\Wolf\\users'
name = socket.gethostname()


def listen_sound():
    playsound.playsound('C:/Wolf/bin/listening.wav')


def listen_sound_execute():
    t1 = threading.Thread(target=listen_sound)
    t1.start()


def read_config():
    global name
    config_file = False
    os.chdir(f'{destination_path}\\{socket.gethostname()}')
    for config in os.listdir():
        if config == 'config.json':
            config_file = True
            break

    if config_file == True:
        with open('config.json', 'r', encoding='utf-8') as file:
            file = file.read()
        file2 = eval(file)
        name = file2['name']
        user_config.update({'name': file2['name']})
    else:
        pass


def voice_output_calculator(answer):
    if answer == 'None':
        audiocreated = gTTS(text=f'Sorry, your term did not bring up any calculation result. Please try again',
                            lang='en', slow=False)
    elif answer == 'Error':
        audiocreated = gTTS(text=f"Sorry, your term did not bring up any result. Try simplifying the question.",
                            lang='en', slow=False)
    elif answer == 'penelusuran = False':
        audiocreated = gTTS(text=f"Here are the results from the web. You can read the tip for more efficient result.",
                            lang='en', slow=False)
    elif 'Playing a video' in answer or 'Playing a music' in answer:
        audiocreated = gTTS(text=f"{answer}")
    elif (len(answer) > 10 and not re.match(r'\s*(\d+)\s*', answer)):
        audiocreated = gTTS(text=f"{answer}, {num.randomize}", lang='en', slow=False)
    else:
        for i in answer:
            if i in string.digits:
                audiocreated = gTTS(text=f"The answer is {answer}", lang='en', slow=False)
                break
            else:
                aftermath_text = num.after_search[answer]
                audiocreated = gTTS(text=f"Here are what I found. {aftermath_text}", lang='en', slow=False)
                break
    a = random.randint(1, 999)
    audiocreated.save(f'tts_temp-{a}.mp3')
    playsound.playsound(f'tts_temp-{a}.mp3')
    os.remove(f'tts_temp-{a}.mp3')


def voice(usrinput):
    audiocreated = gTTS(text=f"{usrinput}", lang='en', slow=False)
    audiocreated.save('test.mp3')
    playsound.playsound('test.mp3')
    os.remove('test.mp3')
    return None, usrinput


def basic_tasks(usr_input):
    # I differentiate the voice output from above because the above one is already specific for some
    # questions. It'll produce weird outputs if I were to use above's function.

    if 'what can you do' in usr_input or 'how can you assist me' in usr_input:
        text = f"Hello {name}. I can search the web, open Windows's pre-installed desktop apps, " \
               "make a note for you, telling the weather, and some few more. You can read more on my documentation."
        print(text)  # will return the text to be displayed on the GUI after it's finished.
        voice(text)
        return text  # note to self -> this return will be used to display the text in the GUI

    elif 'who are you' in usr_input or 'what is your name' in usr_input:
        text = f"The name's Wolf. Nice to meet you, {name}!"
        print(text)  # will return the text to be displayed on the GUI after it's finished.
        voice(text)
        return text  # note to self -> this return will be used to display the text in the GUI

    elif 'what is my name' in usr_input or 'how do you call me' in usr_input:
        text = f'I recognize you as {name}. I hope I spelled your name correctly ...'
        print(text)
        voice(text)
        return text

    elif 'tell me a joke' in usr_input or 'amuse me' in usr_input or 'entertain me' in usr_input or 'make me laugh' in usr_input:
        text = jk.jokes()
        print(text)
        voice(text)
        return text

    elif 'how are you' in usr_input:
        text = num.randomize_response()
        print(text)
        voice(text)
        return text

    return ''


def output(userinput):
    # setting the name of the user to their saved configuration
    read_config()

    # preserving the input before splitting it
    rawinput = userinput

    try:
        # I separated the basic_tasks and the search function to ease the management of the codes
        # it was confusing as heck before I split them into their own respective functions.
        init = basic_tasks(userinput)
        if init != '':
            return None, init
        else:
            pass

        # I also separated the weather input so that it's easier to manage
        weather_check = wt.check_userinput(userinput)
        if weather_check[0] >= 3:
            this_list = wt.weather(weather_check)
            new_string = f'The current weather of {this_list[0]}, {this_list[1]} is {this_list[5]}, with the temperature of {this_list[2]}°C/{this_list[3]}°F'
            print(this_list)
            print(new_string)
            return wt.voice_output_weather(new_string), this_list
        else:
            pass

        # also the time
        check_time = day.check_userinput(userinput)
        if type(check_time) == str:
            voice_asis = day.voice_output_time(check_time)
            return None, voice_asis
        else:
            if check_time >= 2:
                time = day.day_now()
                print(time[0])
                return day.voice_output_time(time[0]), time
            else:
                pass

        check_note = notes.check_userinput(userinput)
        if check_note[0] >= 3:
            if check_note[-1] == 'view':
                note = notes.note(input_check_result=check_note, input=userinput)
                if 'Here is your note' in note[-1].split(':'):
                    voice('Here is your note.')
                else:
                    voice('No notes found.')
                return note

            elif check_note[-1] == 'make':
                note = notes.note(input_check_result=check_note, input=userinput)
                if 'Done' in note[-1].split('!'):
                    voice('Done! Your note has been created.')
                else:
                    voice('No notes found.')
                return note

            elif check_note[-1] == 'edit':
                return voice(f'Sorry, this feature is not supported yet'), 'Not supported yet.'

            elif check_note[-1] == 'delete':
                note = notes.delete_note()
                if note[-1] == 'Note successfully deleted':
                    voice('Done!')
                else:
                    voice('No notes found.')
                return note
            else:
                pass
        else:
            pass

        open_app = apps.check_userinput(userinput)
        if open_app[0] >= 2:
            os.startfile(num.applications[open_app[-1]])
            return voice(f'Starting {open_app[-1]}'), f'Starting {open_app[-1]}...'

        # splitting the input to make it easier to manage.
        userinput = userinput.split()
        print(userinput)

        # checking whether the international_number keys is in userinput or not
        def check_input(userinput):
            for items in userinput:
                if items in num.websites:
                    return False
                else:
                    pass
            for keys in num.international_number.keys():
                if keys in userinput:
                    return True
                else:
                    pass
            return False

        # checking whether the international_number values is in userinput or not
        def check_input_2(userinput):
            for items in userinput:
                if items in num.websites:
                    return False
                else:
                    pass
            for values in num.international_number.values():
                for digits in userinput:
                    for each_digit in digits:
                        if each_digit == str(values):
                            return True
                        else:
                            pass
            return False

        # checking whether the international_operands item is in userinput or not
        def check_input_3(userinput):
            for items in userinput:
                if items in num.websites:
                    return False
                else:
                    pass
            for operand in num.international_operands:
                for operand_2 in userinput:
                    if operand_2 == operand:
                        return True
                    else:
                        pass
            return False

        # for calculating result inputted by the user using the wolfram API
        if check_input_3(userinput) and check_input(userinput) or check_input_3(userinput) and check_input_2(userinput):
            try:
                calculation = ''
                # this for loop is to re-construct the items inside the split 'userinput' into a new string,
                # wolfram doesn't accept list
                for items in userinput:
                    calculation += items + ' '
                app_id = 'AH3H6J-X2E9J7GRV3'
                client = wolframalpha.Client(app_id)
                res = client.query(calculation)
                answer = next(res.results).text
                return voice_output_calculator(answer), f'the answer is {answer}'
            except:
                return voice_output_calculator(
                    'None'), f'Sorry, your term did not bring up any calculation result. Please try again.'

        elif 'who' in userinput or 'what' in userinput or 'define' in userinput:
            try:
                # i am going to use web-scraping using the BeautifulSoup module in this if statement so it can act as a
                # quick explanation to the user if they're lazy enough to read on the web.
                search = ''
                if len(userinput) > 1:
                    for contents in userinput:
                        if contents == 'what':
                            search = 'define '
                        elif contents == 'who':
                            search = 'who is '
                        elif contents == 'is':
                            pass
                        elif contents == 'if':
                            search = 'what happens if '
                        elif contents == 'happened' or contents == 'happen' or contents == 'happens':
                            search = 'what happened '
                        elif contents == 'can':
                            search = 'what can '
                        elif contents == 'will':
                            search = f'{userinput[0]} will '
                        else:
                            search += f'{contents}+'

                    # request to google using 'request' module > extract it to a html using beautifulsoup module > prettify it
                    google_search = requests.get(f'https://www.google.com/search?q={search}')
                    soup = BeautifulSoup(google_search.text, 'html.parser')
                    soup = soup.prettify()
                else:

                    # the only difference with the above section is that if the user only inputted one keyword, it will go
                    # to this section, otherwise it will go to above section
                    search = userinput[-1]
                    google_search = requests.get(f'https://www.google.com/search?q={search}')
                    soup = BeautifulSoup(google_search.text, 'html.parser')
                    soup = soup.prettify()

                # this is where the webscraping comes into play
                scraping = re.findall(r'<div class="BNeawe s3v9rd AP7Wnd">\n\s*(.*?)\n', soup)
                final_scrap = ''
                for items in scraping:

                    # if statement to filter the result. It will pick the first longest sequence of letters.
                    if len(items) > 50:

                        # re to determine a special occasion (ex. title of a person on the first half of the sentence).
                        # it is to prevent the program for cutting the sentence in that title of the person.
                        special_occs = re.findall(r'[A-Z][a-z]{0,3}\.', items)
                        if special_occs == []:
                            special_occs = '. '
                        else:
                            pass
                        final_scrap += items[:items.find('. ', items.index(special_occs[-1]) + 2)] + '.' + '\n'
                        break
                    else:
                        pass

                # calling the gTTS module which will read the scrapped text from the web
                webbrowser.open_new_tab(f'https://www.google.com/search?q={search}')
                return voice_output_calculator(final_scrap), final_scrap
            except:
                voice_output_calculator('Error')
                return None, 'Sorry, your term did not bring up any result. Try simplifying the question.'

        elif userinput[0] or userinput[1] or userinput[2] or userinput[-1] or userinput[-2] in num.predictions:
            # ada_pencarian is for the search term, penelusuran is for the search engine detection. if
            # both return False it'll go to the if statement below.
            ada_pencarian = re.findall(r'\s*(".+")\s*', rawinput)
            penelusuran = False

            # try to find the quotation marks inside the user input. user can use single quote marks to quote
            # stuff instead of using another double quote marks.
            try:
                ada_pencarian = re.findall(r'\s*(".+")\s*', rawinput)[0].replace('"',
                                                                                 '')  # for removing things in rawinput
                penelusuran = re.sub(ada_pencarian, '', rawinput).split()
            except Exception:
                pass

            # the if statement below is the old one without using the double quote marks. My friend tested my program
            # and the easily breaks it by just typing multiple search engines into the command bar. for that he
            # suggested on adding double quote marks for the search term. That's what I did here. The else statement
            # does that.
            if not penelusuran:
                search = ''
                web = 'google'
                browse = ''
                search_check = None
                if 'youtube' and 'music' in userinput or 'yt' and 'music' in userinput:
                    browse = num.searches['youtube']['music']
                    web = 'youtube music'
                    if 'play' in userinput:
                        search_check = 'music'
                elif 'youtube' in userinput or 'yt' in userinput:
                    browse = num.searches['youtube']['youtube']
                    web = 'youtube'
                    if 'play' in userinput:
                        search_check = 'youtube'
                elif 'stack' and 'overflow' in userinput or 'stackoverflow' in userinput:
                    browse = num.searches['stackoverflow']
                    web = 'stackoverflow'
                else:
                    for input in num.searches.keys():
                        if input in userinput:
                            web = input
                            browse = num.searches[web]
                            break
                        else:
                            continue
                    browse = num.searches[web]
                for content in num.yt_case:
                    if content in userinput:
                        userinput.remove(content)
                for prediction in num.predictions:
                    if prediction in userinput:
                        if userinput[0] == 'is':
                            pass
                        else:
                            userinput = list(filter((prediction).__ne__, userinput))
                    else:
                        pass

                for final_items in userinput:
                    search += f'{final_items} '

                if search_check == 'youtube':
                    yt = youtube.playonyt(search)
                    return voice(yt[-1]), yt

                elif search_check == 'music':
                    ytmusic = youtube.play_yt_music(search)
                    return voice(ytmusic[-1]), ytmusic

                else:
                    webbrowser.open_new_tab(f'https://www.google.com/search?q={rawinput}')
                    return voice_output_calculator(
                        'penelusuran = False'), f'Tip: input your search term wrapped in double quotation marks for a specific search engine ' \
                                                f'as shown in the example -> Youtube "brofist". You can see the documentation for a ' \
                                                f'complete list of supported search engines and what to do with them.'
            else:
                # initializing variables
                web = 'google'
                browse = ''
                search_check = None

                # a special case for youtube, yt music, stackoverflow and reddit because they're added last.
                if 'youtube' and 'music' in penelusuran or 'yt' and 'music' in penelusuran:
                    browse = num.searches['youtube']['music']
                    web = 'youtube music'
                    if 'play' in penelusuran:
                        search_check = 'music'
                elif 'youtube' in penelusuran or 'yt' in penelusuran:
                    browse = num.searches['youtube']['youtube']
                    web = 'youtube'
                    if 'play' in penelusuran:
                        search_check = 'youtube'
                elif 'stack' and 'overflow' in penelusuran or 'stackoverflow' in penelusuran:
                    browse = num.searches['stackoverflow']
                    web = 'stackoverflow'
                elif 'reddit' in penelusuran:
                    browse = num.searches['reddit']
                    web = 'reddit'
                else:
                    for input in num.searches.keys():
                        if input in userinput:
                            web = input
                            browse = num.searches[web]
                            break
                        else:
                            continue
                    browse = num.searches[web]
                for prediction in penelusuran:
                    if prediction in num.predictions:
                        penelusuran = list(filter((prediction).__ne__, penelusuran))
                    else:
                        pass

                if search_check == 'youtube':
                    yt = youtube.playonyt(ada_pencarian)
                    return voice(yt[-1]), yt

                elif search_check == 'music':
                    ytmusic = youtube.play_yt_music(ada_pencarian)
                    return voice(ytmusic[-1]), ytmusic

                else:
                    webbrowser.open_new_tab(f'{browse}{ada_pencarian}')
                    print(ada_pencarian)
                    print(penelusuran)
                    return voice(
                        f'Okay, searching "{ada_pencarian}" on {web}'), f'Okay, searching "{ada_pencarian}" on {web}'

        else:
            if 'google' in rawinput:
                rawinput.replace('google', '')
            webbrowser.open_new_tab(f'https://www.google.com/search?q={rawinput}')

    except:
        pass


def voice_input():
    with speech_recognition.Microphone() as input:
        audio_input = sr.listen(input, 2, 5)
        audio_data = ''

        try:
            check_1 = False
            check_2 = False
            check_3 = False
            input_error = True
            counter = 0
            web = 'google'
            audio_data = sr.recognize_google(audio_input).lower()

            for checking in audio_data.split():
                if checking in num.preposition:
                    check_1 = True
                elif checking in num.prediction_2:
                    check_2 = True
                elif checking in num.websites:
                    for website in num.websites:
                        if website == checking:
                            web = website
                            break
                    check_3 = True
                else:
                    pass

            for checking_note in audio_data.split():
                if checking_note in notes.prediction_voice:
                    counter += 1
                else:
                    pass

            if check_1 and check_2 and check_3:
                if 'play' in audio_data.split() and (web == 'youtube' or web == 'music'):
                    voice(f'Okay, what do you want me to play on {web}?')

                    while input_error:
                        try:
                            listen_sound_execute()
                            audio_input_2 = sr.listen(input, 5, 5)
                            audio_data_2 = sr.recognize_google(audio_input_2).lower()
                            input_error = False
                            return audio_data_2, web, 'play'

                        except speech_recognition.UnknownValueError:
                            voice(f'Sorry, I didn\'t get that. Please try saying it again.')

                        except speech_recognition.RequestError:
                            return 'maintenance', 'maintenance', 'maintenance'

                else:
                    voice(f'Okay, what do you want me to search on {web}?')
                    while input_error:
                        try:
                            listen_sound_execute()
                            audio_input_2 = sr.listen(input, 5, 5)
                            audio_data_2 = sr.recognize_google(audio_input_2).lower()
                            input_error = False
                            return audio_data_2, web, 'search'

                        except speech_recognition.UnknownValueError:
                            voice(f'Sorry, I didn\'t get that. Please try saying it again.')

                        except speech_recognition.RequestError:
                            return 'maintenance', 'maintenance', 'maintenance'

            elif counter >= 3:
                voice(f'Okay, what do you want me to write on your note?')
                while input_error:
                    try:
                        listen_sound_execute()
                        audio_input_2 = sr.listen(input, 5, 5)
                        audio_data_2 = sr.recognize_google(audio_input_2).lower()
                        input_error = False
                        return audio_data_2, 'note', 'note'

                    except speech_recognition.UnknownValueError:
                        voice(f'Sorry, I didn\'t get that. Please try saying it again.')

                    except speech_recognition.RequestError:
                        return 'maintenance', 'maintenance', 'maintenance'

            else:
                pass

        except speech_recognition.UnknownValueError:
            return 'error', 'error', 'error'

        except speech_recognition.RequestError:
            return 'maintenance', 'maintenance', 'maintenance'

        return audio_data, 'output', 'output'


"""
time.sleep(1)
while 1:
    input_temp = input('enter your question')
    output(input_temp)
# """
