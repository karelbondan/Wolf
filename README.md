# Wolf

The final project for Introduction to Programming / Program Design Methods - Binus University<br/>
2020/2021

### What is Wolf?

Wolf is a virtual assistant program written in Python, as you can see on the right side of this note.
Wolf also features user interface. User can customize some of Wolf's features such as their name,
their preffered background color, and their profile picture.

### Features (as of 31st December 2020)

1. Define something
2. Give short description of known people
3. Make a note
4. Open user-installed apps
5. Search the web (multiple search engines)
6. Telling current weather of a city
7. Telling jokes
8. Voice commands
9. User interface
10. Play video on YouTube & music on YT Music based on user search

### Current state

This project is unfinished. Minor updates will come later when the feature has been implemented (you can
read on the bottommost of this note). I don't plan to continue adding features too (might change my mind later.
If ever I don't have anything to do, maybe I'll try implementing more stuff into Wolf).

### Bugs

- Defining something can sometimes be buggy, as it gives the explanation on other language other than English, depends
on the user's locale language. The same bug goes for giving description of someone.
  
- Before Wolf has finished talking, the GUI will be frozen. I'll try to fix this later if time and luck can cooperate.

### Important Note

If someone somehow finds this and wants to clone this repo, Wolf only works on Windows and you need to install some depedencies if you haven't:
- [PyAudio](https://pypi.org/project/PyAudio/) (If you have any errors on installing, [go to this page](https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14))
- [playsound](https://pypi.org/project/playsound/)
- [gTTS](https://pypi.org/project/gTTS/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [PySide2](https://pypi.org/project/PySide2/)
- [opencv](https://pypi.org/project/opencv-python/)
- [Pillow](https://pypi.org/project/Pillow/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [wolframalpha](https://pypi.org/project/wolframalpha/)

If you've met the first requirement (you're using Windows) and have installed the depedencies, please move or copy the 'Wolf'
folder to the C:/ drive (the C:/ itself, don't put it on any folder). This program was made on Windows 10 and uses file modifications, 
so all the files and folders necessary for this program to run is referenced to Windows 10. If you're using an older version,
feel free to try it. Important note is that I haven't tested this on the older version of Windows, so the program may not work
correctly (especially on first launch), you may get blank user profile image on the top right of the GUI and on the user settings
page.</br>
> ps. You can always change your profile picture and Wolf will remember your changes.

```
WIP (ignore) [All done]

- weather icons -> DONE, 29th Dec 2020.
- usr img on start -> DONE, 29th Dec 2020.
- save user settings upon exit -> DONE, 30th Dec 2020.
- threading (if can lol, gave up with the alarm); voice and gui work together -> discarded.
- open app -> DONE, 31st Dec 2020
- fix path -> DONE, 29th Dec 2020.
- make list, note -> list feature discarded (time isn't enough :<), note -> DONE, 31st Dec 2020
- expand time feature (if can) -> discarded.
- make the bg color stays the same if ever the user changed the color -> DONE, 30th Dec 2020.
- make the profile pic and name stays the same if ever the user changes those -> DONE, 29th Dec 2020, 30th Dec 2020.
- save user's name to a file and open in assistant file -> DONE, 31st Dec 2020
- ATUR FILE WOI HADEH -> DONE, 31st Dec 2020
- Differentiate between text input and voice input -> Text input DONE, 31st Dec 2020; Voice input DONE, 1st Jan 2021
- Add background listening function -> okay yeah, maybe the final final one. -> DONE, 2nd Jan 2021
```
