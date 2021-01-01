import time

import pyautogui
import speech_recognition
import os
import socket

sr = speech_recognition.Recognizer()
calling = ['woof woof', 'hey wolf', 'hey woof', 'wolf wolf', 'hello wolf', 'hey google', 'ok google']


while True:
    with open(f'C:/Wolf/users/{socket.gethostname()}/config.json') as mic_name:
        microphone = eval(mic_name.read())
        microphone = microphone['stylesheet']
        print(microphone)

    def find_mic():
        mic_attempt_one = pyautogui.locateOnScreen(f'C:/Wolf/bin/microphones/{microphone}.png', confidence=.9)
        return mic_attempt_one


    def find_icon_light():
        locate_light_taskbar = pyautogui.locateOnScreen('C:/Wolf/bin/taskbar_light.png', confidence=.9)
        return locate_light_taskbar


    def find_icon_dark():
        locate_dark_taskbar = pyautogui.locateOnScreen('C:/Wolf/bin/taskbar_dark.png', confidence=.9, grayscale=False)
        return locate_dark_taskbar

    try:
        with speech_recognition.Microphone() as input:
            print('listening...')
            audio_input = sr.listen(input, 2, 2)

            try:
                audio_data = sr.recognize_google(audio_input).lower()
                print(audio_data)
                if audio_data in calling:
                    print("Woof woof! I'm here!")

                    try:
                        mic_attempt_one = find_mic()
                        if mic_attempt_one == None:
                            raise FileNotFoundError
                        else:
                            pyautogui.click(mic_attempt_one)

                    except:
                        try:
                            taskbar_light = find_icon_light()
                            if taskbar_light == None:
                                raise FileNotFoundError
                            else:
                                pyautogui.click(taskbar_light)

                                mic = find_mic()
                                pyautogui.click(mic)

                        except:
                            dark_taskbar = find_icon_dark()
                            pyautogui.click(dark_taskbar)

                            mic = find_mic()
                            pyautogui.click(mic)
                    time.sleep(13)
                else:
                    print("i'm not called yet... waiting to be called...")

            except:
                print("no input found. retrying in 0.2 seconds.")

    except:
        print('no input found. listening...')
