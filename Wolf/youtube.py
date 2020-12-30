import requests
import webbrowser


# I found this function below on a module called PyWhatKit. instead of installing I only picked this one
# particular function. The function underneath below function is the one I defined myself. The function below
# can be found at https://github.com/Ankit404butfound/PyWhatKit/blob/master/pywhatkit/mainfunctions.py

def playonyt(topic):
    url = 'https://www.youtube.com/results?q=' + topic
    count = 0
    cont = requests.get(url)
    data = str(cont.content)
    lst = data.split('"')
    for i in lst:
        count += 1
        if i == 'WEB_PAGE_TYPE_WATCH':
            print(count)
            break
    if lst[count - 5] == "/results":
        return 'sorry, I didn\'t find any video that matches your search result.'

    print("Videos found, opening most recent video")
    webbrowser.open("https://www.youtube.com" + lst[count - 5])
    return 'playing a video of'


def play_yt_music(usrinput):
    pass
