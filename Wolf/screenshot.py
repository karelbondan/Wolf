import pyautogui
import os
import re
import pygetwindow

# prediction list if user wants to ss the screen
predictions = ['take', 'a', 'screenshot', 'my', 'the', 'screen', 'window', 'app']

# if these indexes are in the search input then user is not trying to ss the screen
abort = ['how', 'search', 'to']


def screenshot():
    images = ''

    # change dir to ss default location, listing the existing screenshots
    os.chdir(f'{os.environ["USERPROFILE"]}\\Pictures\\Screenshots')
    for image in os.listdir():
        images += f'{image} '

    # finding the numbers
    screenshots = re.findall(r'\s*\((\d*)\)', images)

    # converting numbers to int
    latest_screenshot = [int(screenshot) for screenshot in screenshots]

    # getting the highest number, increment by 1, screenshot
    pyautogui.screenshot(f'Screenshot ({max(latest_screenshot) + 1}).png')


def main():
    # getting the hwnd ID of the assistant program
    wolf = pygetwindow.getWindowsWithTitle('Wolf - Assistant')[0]

    # minimize
    wolf.minimize()

    # try screenshot, if folder not found create one
    try:
        screenshot()
        return None, f'Done!'

    except FileNotFoundError:
        os.chdir(f'{os.environ["USERPROFILE"]}\\Pictures\\')
        os.mkdir('Screenshots')
        screenshot()
        return None, f'Done!'

    # microsoft somehow moved the pictures folder to onedrive,
    # it'll return this if above handlers failed.
    except:
        return None, f'{os.environ["USERPROFILE"]}\\Pictures folder not found, please read the documentation to fix it.'


# check input, if counter >= 3 it'll screenshot
def check_userinput(input):
    counter = 0
    user_input = input.split()
    for prediction in user_input:
        if prediction in predictions:
            counter += 1
        elif prediction in abort:  # if any of abort's indexes are in user input then abort
            counter = 0
            break
        else:
            pass
    return counter
