import requests
import webbrowser
from bs4 import BeautifulSoup


# I found this function below on a module called PyWhatKit. instead of installing I only picked this one particular
# function. The function underneath below function is the one I defined myself. The function below can be found at
# https://github.com/Ankit404butfound/PyWhatKit/blob/master/pywhatkit/mainfunctions.py. I'll try explaining on
# comments on how the function below works. I only modify the return value of the function a bit for obvious reasons.
# (keeping the originality of the source code and respecting the developer, Ankit).

def playonyt(topic):
    # url for request module.
    url = 'https://www.youtube.com/results?q=' + topic

    # counter for later purpose on finding the link of the video.
    count = 0

    # web scraping and splitting the data based on double quote marks.
    cont = requests.get(url)
    data = str(cont.content)
    lst = data.split('"')

    # looping until it finds the specific string below.
    for i in lst:
        count += 1
        if i == 'WEB_PAGE_TYPE_WATCH':
            break

    # if not result: return 'no videos found'.
    if lst[count - 5] == "/results":
        return None, 'sorry, I didn\'t find any video that matches your search result.'

    # playing the video
    print("Videos found, opening most recent video")
    webbrowser.open("https://www.youtube.com" + lst[count - 5])

    return None, f'Playing a video based on your search:\n\n"{topic}"'


# this function below is the one I defined myself, I used Ankit's (PyWhatKit module developer) technique
# on getting the music link by using counter. But because the system of YouTube Music is somehow different
# from YouTube, I have to first encode the result then decode it again because there are unicode escapes.

def play_yt_music(usrinput):
    # an empty list for storing the strings found by the request module.
    unfiltered_contents = []

    # a counter to count how many times it loops until it found a specific string.
    counter = 0

    # the url for the request module to get the data.
    url = f'https://music.youtube.com/search?q={usrinput}'

    # the default header (browser version) of the default request browser simulation is so old even the url refuse
    # to view the page lmao. the headers dict below is to 'update' the browser simulation of request.
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 RuxitSynthetic/1.0 v7984376556 t38550 ath9b965f92 altpub cvcv=2'}

    # web scraping.
    music_search = requests.get(url, headers=headers)
    soup = BeautifulSoup(music_search.text, 'html.parser')

    # encode, decode (because there are unicode chars), and splitting it on double quote marks.
    soup = soup.prettify().encode()
    soup = soup.decode('unicode_escape')
    soup = soup.split('"')

    # looping until it finds that specific string which will be the target to find the music link.
    for musicid in soup:
        counter += 1
        unfiltered_contents.append(musicid)
        if musicid == 'MUSIC_VIDEO_TYPE_ATV':
            break

    # if len not 11 return link not found
    if len(unfiltered_contents[counter - 17]) != 11:
        return None, f'No music found. Please retry your search'
    else:
        pass

    # debugging
    """
    print(unfiltered_contents)
    print(unfiltered_contents[counter - 17])
    print(len(unfiltered_contents[counter - 17]))
    print(counter)
    """

    # playing the music
    webbrowser.open(f'https://music.youtube.com/watch?v={unfiltered_contents[counter - 17]}')

    return None, f'Playing a music based on your search:\n\n"{usrinput}"'


# debugging
"""
playonyt('dream 4 hunters vs speedrunner finale rematch')
play_yt_music('and so we fall the stupendium')
"""
