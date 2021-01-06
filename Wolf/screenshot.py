import pyautogui
import os
import re
import pygetwindow

predictions = ['take', 'a', 'screenshot', 'my', 'the', 'screen', 'window', 'app']


def screenshot():
    images = ''
    os.chdir(f'{os.environ["USERPROFILE"]}\\Pictures\\Screenshots')  # change dir to ss default location
    for image in os.listdir():
        images += f'{image} '
    screenshots = re.findall(r'\s*\((\d*)\)', images)  # finding the numbers
    latest_screenshot = [int(screenshot) for screenshot in screenshots]  # converting numbers to int

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
        else:
            pass
    return counter
