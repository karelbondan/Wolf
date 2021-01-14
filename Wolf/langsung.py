# all statements and functions in this library is literally the same as in assistant file, but without the voice output.
# i tried to mimic google assistant's behavior where if user isn't saying anything and just type it into the search bar,
# google will keep quiet and just directly show the result. this library here is the exact same thing as that.
# less comments will be put here as you can read the explanation already on the assistant library.

import os
import re
import socket
import pygetwindow
import time
import webbrowser
import requests
import wolframalpha
from bs4 import BeautifulSoup
import checking as num
import day
import jokes as jk
import notes
import screenshot
import weather as wt
import apps
import youtube
import system

# dict to store user's name later on.
user_config = {}

# path containing user's config.
destination_path = f'C:\\Wolf\\users'

# the initial variable and user's default name.
name = socket.gethostname()


# function to get user's name.
def read_config():
    # global the name so the variable can be used on other functions.
    global name

    # checking whether the config file exists or not.
    config_file = False

    # changing the working path and listing the files.
    os.chdir(f'{destination_path}\\{socket.gethostname()}')
    for config in os.listdir():
        if config == 'config.json':
            config_file = True
            break

    # setting user's name if config file is available
    if config_file == True:
        with open('config.json', 'r', encoding='utf-8') as file:
            file = file.read()
        file2 = eval(file)
        name = file2['name']
        user_config.update({'name': file2['name']})
    else:
        pass


# basic tasks and questions
def basic_tasks(usr_input):
    if usr_input == 'hi' or usr_input == 'hello':
        text = 'Hello, how can I help you today?'
        print(text)
        return text

    elif 'what can you do' in usr_input or 'how can you assist me' in usr_input:
        text = f"Hello {name}. I can search the web, open Windows's pre-installed desktop apps, " \
               "make a note for you, telling the weather, and some few more. You can read more on my documentation."
        print(text)  # will return the text to be displayed on the GUI after it's finished.
        return text  # note to self -> this return will be used to display the text in the GUI

    elif 'who are you' in usr_input or 'what is your name' in usr_input:
        text = f"The name's Wolf. Nice to meet you, {name}!"
        print(text)  # will return the text to be displayed on the GUI after it's finished.
        return text  # note to self -> this return will be used to display the text in the GUI

    elif 'what is my name' in usr_input or 'how do you call me' in usr_input:
        text = f'I recognize you as {name}. I hope I spelled your name correctly ...'
        print(text)
        return text

    elif 'tell me a joke' in usr_input or 'amuse me' in usr_input or 'entertain me' in usr_input or 'make me laugh' in usr_input:
        text = jk.jokes()
        print(text)
        return text

    elif 'how are you' in usr_input:
        text = num.randomize_response()
        print(text)
        return text

    return ''


# main function
def output(userinput):
    # setting the name of the user to their saved configuration
    read_config()

    # preserving the input before splitting it
    rawinput = userinput

    try:
        # separated the basic_tasks and the search function to ease the management of the codes
        # it was confusing as heck before I split them into their own respective functions.
        init = basic_tasks(userinput)
        if init != '':
            return None, init
        else:
            pass

        # separated the weather input so it's easier to manage
        weather_check = wt.check_userinput(userinput)
        if weather_check[0] >= 3:
            this_list = wt.weather(weather_check)
            new_string = f'The current weather of {this_list[0]}, {this_list[1]} is {this_list[5]}, with the temperature of {this_list[2]}°C/{this_list[3]}°F'
            print(this_list)
            print(new_string)
            return None, this_list
        else:
            pass

        # separated the time function
        check_time = day.check_userinput(userinput)
        if type(check_time) == str:
            return None, check_time
        else:
            if check_time >= 2:
                time = day.day_now()
                return None, time[-1]
            else:
                pass

        # make/delete notes check
        check_note = notes.check_userinput(userinput)
        if check_note[0] >= 3:
            print(check_note)
            if check_note[-1] == 'view':
                return notes.note(input_check_result=check_note, input=userinput)
            elif check_note[-1] == 'make':
                return notes.note(input_check_result=check_note, input=userinput)
            elif check_note[-1] == 'edit':
                return None, 'Not supported yet.'
            elif check_note[-1] == 'delete':
                return notes.delete_note()
            else:
                pass
        else:
            pass

        # open apps check
        open_app = apps.check_userinput(userinput)
        if open_app[0] >= 3:
            if open_app[-1] == 'open':
                try:
                    os.startfile(num.applications[open_app[1]])
                    return None, f'Starting {open_app[1].capitalize()}...'

                except KeyError as err:
                    print(err)
                    return None, f'App not supported yet'

            elif open_app[-1] == 'close':
                dbl_backslash = '\\'
                app = num.applications[open_app[1]].rfind(dbl_backslash)

                try:
                    kill = os.system(
                        f'TASKKILL /F /IM {num.applications[open_app[1]][app:].replace(dbl_backslash, "")}')
                    if kill == 128:
                        raise apps.AppNotFoundError(f'{open_app[1]}')
                    if open_app[1] == 'explorer':
                        os.startfile('explorer.exe')
                    return None, f'Closing {open_app[1].capitalize()}...'

                except apps.AppNotFoundError as err:
                    print(err)
                    return None, f'{open_app[1].capitalize()} is not running. You can start it by typing "start {open_app[1]}"'

        # screenshot check
        snap = screenshot.check_userinput(userinput)
        if snap >= 3:
            shot = screenshot.main()
            return None, shot[-1]

        # system check (for shut down and restart)
        sys_check = system.check_input(userinput)
        if sys_check[0] >= 3:
            if sys_check[-1] == 'shutdown':
                return os.system('shutdown /s /t 5'), f'Shutting down system in 5 seconds...'
            elif sys_check[-1] == 'restart':
                return os.system('shutdown /r /t 5'), f'Restarting system in 5 seconds...'

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
                return None, f'the answer is {answer}'
            except:
                return None, f'Sorry, your term did not bring up any calculation result. Please try again.'


        elif 'who' in userinput or 'what' in userinput or 'define' in userinput:
            header = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7,zh-TW;q=0.6,zh-CN;q=0.5,zh;q=0.4,ja-JP;q=0.3,ja;q=0.2',
                'cookie': 'CGIC=EhQxQzFDSFdMX2VuSUQ5MDJJRDkwMiKHAXRleHQvaHRtbCxhcHBsaWNhdGlvbi94aHRtbCt4bWwsYXBwbGljYXRpb24veG1sO3E9MC45LGltYWdlL2F2aWYsaW1hZ2Uvd2VicCxpbWFnZS9hcG5nLCovKjtxPTAuOCxhcHBsaWNhdGlvbi9zaWduZWQtZXhjaGFuZ2U7dj1iMztxPTAuOQ; CONSENT=YES+ID.en+202004; OGPC=19022270-1:; SEARCH_SAMESITE=CgQIyZEB; SID=5gc_fzvC7ld4U-3DPbiZdOCyYdzIzieEtxU47HYhBYHbDxUwGfvbnETbq05rJeB0Y21Pdw.; __Secure-3PSID=5gc_fzvC7ld4U-3DPbiZdOCyYdzIzieEtxU47HYhBYHbDxUwvXFS3hrMrMTFKqLYDLgzdA.; HSID=A5iUgyphfucSjbKOO; SSID=AQ1BbmPS5Mt8G3EH7; APISID=cZzg5fr40eC8gTq1/AMJKcCib6RsfZ1vKY; SAPISID=Jp7fgDOt3axBtUnp/A3rSfLiBWDVaxFz1j; __Secure-3PAPISID=Jp7fgDOt3axBtUnp/A3rSfLiBWDVaxFz1j; ANID=AHWqTUkY4fCAmJvhTm5bEJTidemDLdOUftNUhygn0309rLQdQmeCibUPCk6wNMRn; OTZ=5802877_28_28__28_; NID=207=Ma74myQrby8mAAAHUVXhlLc84trJBQv5L8wOd9O4GAVAnelqDyNRbK7IV0PHWzgUtZA_hLg_HwJ7SAsBaIHNpVjHV3iKyQ9S-TBqFahYHZFwmdDzG1OIdLBjRkGWgzI2D7h11Tvx1UzCqhB8nVz52iRsOJAzw5E9KC0mNp4kIb6Akwsh3nEbMgx033EqLhc-03_Dfs9Czfy3p8xteb_CHFW80kFmqpIvTfBqHTNALUZFUVqmLpacCa1rOQdiNQV6rpq2Gd-0wRi1MA2p-ENq8OAw9AJqs_BhIARN_ui7ZuBw44QFgUxZ9b-7wjgBDG8d5FBi-eAmP_PGatm52HiigWrhB_FfPLSCDK63AJUrEKp0GdYziWsDR3mV1NsU6B7NDptQUeCm; 1P_JAR=2021-01-14-12; DV=czkrUL6j19dPwGsmhb-xJuUDSX0OcJc3mRwa6ZImqAAAAMBLUjyomhJKagAAAJA7uHL3LJt1HAAAAA; SIDCC=AJi4QfEOlVxJy8NFJF3vlfVuWBt5M5b93oS6ETRZgVUXs8-j8U8jkChuYObW-YplhopLpkBGCw; __Secure-3PSIDCC=AJi4QfE1rAuCEUH4TdOd1ktnYUt-OnEoXhByQz4hTT7RFQtfG-QnTKRQhTEv4SSq4FLxkGT5n38',
                'referer': 'https://www.google.com/',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1'}
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
                    google_search = requests.get(f'https://www.google.com/search?q={search}', headers=header)
                    soup = BeautifulSoup(google_search.text, 'html.parser')
                    soup = soup.prettify()
                else:

                    # the only difference with the above section is that if the user only inputted one keyword, it will go
                    # to this section, otherwise it will go to above section
                    search = userinput[-1]
                    google_search = requests.get(f'https://www.google.com/search?q={search}', headers=header)
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
                return None, final_scrap
            except Exception as e:
                print(e)  # debugging
                return None, 'Sorry, your term did not bring up any result. Try simplifying the question.'

        # elif 'make' in userinput and 'alarm' in userinput or 'new' in userinput and 'alarm' in userinput:
        # print("This is an alarm test!")

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
                webbrowser.open_new_tab(f'https://www.google.com/search?q={rawinput}')
                return None, f'Tip: input your search term wrapped in double quotation marks for a specific search engine ' \
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

                # __ne__ is to delete all occurring things that are present in the list if it's present in the
                # prediction list, this is why the for loop is necessary
                for prediction in penelusuran:
                    if prediction in num.predictions:
                        penelusuran = list(filter(prediction.__ne__, penelusuran))
                    else:
                        pass

                if search_check == 'youtube':
                    yt = youtube.playonyt(ada_pencarian)
                    return yt

                elif search_check == 'music':
                    ytmusic = youtube.play_yt_music(ada_pencarian)
                    return ytmusic

                else:
                    webbrowser.open_new_tab(f'{browse}{ada_pencarian}')
                    print(ada_pencarian)
                    print(penelusuran)
                    return None, f'Okay, searching "{ada_pencarian}" on {web}'

        else:
            if 'google' in rawinput:
                rawinput.replace('google', '')
            webbrowser.open_new_tab(f'https://www.google.com/search?q={rawinput}')
    except:
        pass


# debugging
"""
time.sleep(1)
while 1:
    input_temp = input('enter your question')
    output(input_temp)
# """
