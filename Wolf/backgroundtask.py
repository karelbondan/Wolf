import time
import pyautogui
import speech_recognition
import os
import socket
import pygetwindow
import random  # for debugging

# speech recognition init
sr = speech_recognition.Recognizer()

# prediction list
calling = ['woof', 'wolf', 'wolves', 'walf', 'wilf', 'woof woof', 'wolf wolf', 'wall', 'well']


# restore or activate (focus on) the program
def check_window():
    wolf = pygetwindow.getWindowsWithTitle('Wolf - Assistant')[0]
    print(wolf)
    print(wolf.isActive)
    print(wolf.isMinimized)
    if wolf.isMinimized:
        wolf.restore()
    if not wolf.isActive:
        wolf.minimize()
        wolf.restore()
    else:
        pass


# main loop
time.sleep(1.3)
while True:
    try:
        # socket.gethostname() gets the pc's name
        with open(f'C:/Wolf/users/{socket.gethostname()}/config.json') as mic_name:
            microphone = eval(mic_name.read())
            microphone = microphone['stylesheet']
            print(microphone)
    except FileNotFoundError:
        microphone = 'turqoise'  # the default style
        print(microphone)

    # finding the mic button
    def find_mic():
        mic_attempt_one = pyautogui.locateOnScreen(f'C:/Wolf/bin/microphones/{microphone}.png', confidence=.9)
        return mic_attempt_one


    try:
        with speech_recognition.Microphone() as input:
            print(f'{random.randint(0,100)} - listening...')
            audio_input = sr.listen(input, 2.5, 2.5)  # input, waiting input timeout, speech timeout

            try:
                audio_data = sr.recognize_google(audio_input).lower()
                print(audio_data)
                if audio_data in calling:
                    print("Woof woof! I'm here!")

                    try:
                        mic_attempt_one = find_mic()

                        # raises error when it doesn't find the mic button, else click the button
                        if mic_attempt_one == None:
                            raise FileNotFoundError
                        else:
                            pyautogui.click(mic_attempt_one)

                    except:
                        try:
                            check_window()
                            mic = find_mic()
                            pyautogui.click(mic)

                        except:  # attempt the second time when it fails to find the window
                            check_window()
                            mic = find_mic()
                            pyautogui.click(mic)

                    # pausing to let the assistant program execute first; this program isn't in sync
                    time.sleep(5)

                else:
                    print("i'm not called yet... waiting to be called...")

            except:
                print("no input found. retrying in 0.2 seconds.")

    except:
        print('no input found. listening...')
