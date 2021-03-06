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
11. Shut down and restart system
12. Always listen in background, user can call Wolf by using "wake up phrase"

### Current state

This project is finished for now. This thing has chipped away my sanity long enough, time to say goodbye to it.
I don't plan on adding features as of now (might change my mind later;
If ever I don't have anything to do, maybe I'll try implementing more stuff into Wolf).

### Bugs

- Giving description of someone sometimes uses user's locale language.
  
- Before Wolf has finished talking, the GUI will be frozen.

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
- [pygetwindow](https://pypi.org/project/PyGetWindow/)
- [App Fonts](https://drive.google.com/file/d/1h_c5Ypzeo20X1mUfyXXnFgzDQKQ82MLE/view?usp=sharing) (Please install all fonts that are in this archive)

If you've met the first requirement (you're using Windows) and have installed the depedencies, please move or copy the 'Wolf'
folder to the C:/ drive (the C:/ itself, don't put it on any folder). </br>

> Launch this program by running ```main.py```</br>

This program was made on Windows 10 and uses file modifications, 
so all the files and folders necessary for this program to run is referenced to Windows 10. If you're using an older version,
feel free to try it. Important note is that I haven't tested this on the older version of Windows, so the program may not work
correctly (especially on first launch), you may get blank user profile image on the top right of the GUI and on the user settings
page.</br>

> ps. You can always change your profile picture and Wolf will remember your changes.
