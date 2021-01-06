# Base by Wanderson M. Pimenta
# Mass-modification by Karel Bondan
# Project made with: Qt Designer and PySide2

import sys
import platform
import PyQt5
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent, QTimer)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QPainterPath)
from PySide2.QtWidgets import *
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import cv2
import re
import os
import shutil
import gui
import day
import assistant as assist
import time
import socket
import init
import atexit
import langsung
import playsound
import threading
import ctypes
import subprocess
import signal

# GUI file, includes the main interface template, which of course I made myself using the
# PySide2 Designer program came together with the installed module.
import screenshot
from gui import Ui_MainWindow

# Import functions to make the default window border and title bar
# be replaced with my custom title bar and border.
from fungsi import *

# initial configurations
user_config = {}  # will include user configurations: theme color, user name, and tip

# stylesheet, name, and tip will be used later to save the user configuration
stylesheet = ''
name = ''
tip = True

# the default destination path for this whole program
destination_path = f'C:\\Wolf\\users'

# the image path which will be used later to determine the user's profile picture on Windows.
image_change_path = None

# a dictionary containing the theme color configurations.
background_colors = {
    'atlas': 'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254, 172, 94, 255), stop:0.488636 rgba(199, 121, 208, 255), stop:1 rgba(75, 192, 200, 255));',
    'biruish': 'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00568182 rgba(65, 146, 189, 255), stop:1 rgba(55, 85, 151, 255));',
    'darkknight': 'background-color: qlineargradient(spread:pad, x1:0, y1:0.455, x2:1, y2:0.875, stop:0 rgba(186, 139, 2, 255), stop:1 rgba(24, 24, 24, 255));',
    'grayscale': 'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(26, 26, 26, 255));',
    'hersheys': 'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(30, 19, 12, 255), stop:1 rgba(154, 132, 120, 255));',
    'lime': 'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(59, 150, 70, 255), stop:1 rgba(188, 182, 0, 255));',
    'lizard': 'background-color: qlineargradient(spread:pad, x1:0, y1:0.471, x2:1, y2:0.636, stop:0 rgba(48, 67, 82, 255), stop:1 rgba(215, 210, 204, 255));',
    'nightday': 'background-color: qlineargradient(spread:pad, x1:0, y1:0.193, x2:1, y2:0.546, stop:0 rgba(44, 62, 80, 255), stop:1 rgba(52, 152, 219, 255));',
    'passion': 'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(229, 57, 53, 255), stop:1 rgba(227, 93, 91, 255));',
    'piglet': 'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(238, 156, 167, 255), stop:1 rgba(227, 93, 91, 255));',
    'predawn': 'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 161, 127, 255), stop:1 rgba(0, 34, 62, 255));',
    'purplish': 'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(109, 73, 188, 255), stop:1 rgba(52, 40, 124, 255));',
    'sagepersuasive': 'background-color: qlineargradient(spread:pad, x1:0, y1:0.403, x2:1, y2:0.636455, stop:0 rgba(204, 204, 178, 255), stop:1 rgba(117, 117, 25, 255));',
    'sunset': 'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(220, 71, 71, 255), stop:1 rgba(76, 59, 125, 255));',
    'thestrain': 'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(135, 0, 0, 255), stop:1 rgba(25, 10, 5, 255));',
    'timber': 'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(252, 0, 255, 255), stop:1 rgba(0, 219, 222, 255));',
    'tree': 'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(237, 229, 0, 255), stop:1 rgba(113, 63, 64, 255));',
    'turqoise': 'background-color: qlineargradient(spread:pad, x1:0, y1:0.455, x2:1, y2:0.733, stop:0 rgba(19, 106, 138, 255), stop:1 rgba(38, 120, 113, 255));',
    'vine': 'background-color: qlineargradient(spread:pad, x1:0, y1:0.455, x2:1, y2:0.773, stop:0 rgba(0, 191, 143, 255), stop:1 rgba(0, 21, 16, 255));', }

# telling Windows that this is a different process so the icon can be set
myappid = u'wolf.wolf.assistant.1.0.0'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


# the main user interface class
class MainWindow(QMainWindow):
    # initial constructor
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # summoning the splash screen
        self.splash = subprocess.Popen('python splash.py', shell=True,
                                       creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

        # default self variables
        self.ui.user_name.setText(socket.gethostname())
        self.stylesheet = 'turqoise'
        self.name = socket.gethostname()
        self.tip = True
        self.timer = 0

        # setting the app icon to show on the taskbar
        self.setWindowIcon(QtGui.QIcon('C:/Wolf/bin/icon.ico'))

        # method to summon the background process
        def always_listen():
            listen = subprocess.Popen('python backgroundtask.py', shell=True,
                                      creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
            return listen

        # method to kill the background process when the main GUI is exited
        def kill_child(child_pid):
            proc_pid = child_pid.pid
            if proc_pid is None:
                pass
            else:
                child_pid.send_signal(signal.CTRL_BREAK_EVENT)

        # these two method below has to be separated so it can fit inside the lambda function, since
        # threading only accepts functions
        def listen_sound():
            playsound.playsound('C:/Wolf/bin/listening.wav')

        def listen_sound_execute():
            t1 = threading.Thread(target=listen_sound)
            t1.start()

        def shot_voice(voice):
            voice = threading.Thread(target=assist.voice, args=[f'{voice[-1]}'])
            voice.start()

        # setting the welcome screen based on the current user pc time
        def greeting():
            self.ui.init.show()
            time_now = int(time.strftime('%H'))
            if 0 <= time_now <= 11:
                self.ui.init.setText(f'Good morning, {self.name}.\nYour wish is my command.')
            elif time_now < 18:
                self.ui.init.setText(f'Good afternoon, {self.name}.\n Your wish is my command.')
            elif time_now >= 18:
                self.ui.init.setText(f'Good evening, {self.name}.\nYour wish is my command.')
            else:
                self.ui.init.setText(f'Welcome back, {self.name}.\nYour wish is my command.')

        # method to move the window when dragged by left mouse on the title bar
        def move_window(event):
            # moves the windows if the left mouse button is pressed
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # variable to make the move_window above works
        self.ui.frame_appcontrol.mouseMoveEvent = move_window

        # a method to set the stylesheet when user presses the button.
        def set_style(stylename):
            global stylesheet
            self.ui.all_content.setStyleSheet(background_colors[stylename])
            self.stylesheet = stylename
            stylesheet = self.stylesheet
            save_config(stylesheet=self.stylesheet, name=self.name, tip=self.tip)
            print(f'Success! Background color set to {stylename}')
            print(self.stylesheet)

        # a method to make the picture picked by the user and or initializing user's picture on every launch as
        # a rounded user profile picture on the user configuration page, does not affect the original file.
        # will set the size to 300x300 pixels.
        def round_avatar(paths):
            self.target = QtGui.QPixmap(300, 300)
            self.target.fill(QtCore.Qt.transparent)
            p = QtGui.QPixmap(paths).scaled(
                300, 300, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)

            painter = QtGui.QPainter(self.target)
            painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
            painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing, True)
            painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)

            path = QtGui.QPainterPath()
            path.addRoundedRect(0, 0, 300, 300, 150, 150)

            painter.setClipPath(path)
            painter.drawPixmap(0, 0, p)
            self.ui.profile_change.setIcon(self.target)

        # a method to make the picture picked by the user and or initializing user's picture on every launch as
        # a rounded picture used as the icon of the user configuration button, does not affect the original file.
        # will set the size to 56x56 pixels.
        def round_avatar_icon(paths):
            self.target = QtGui.QPixmap(56, 56)
            self.target.fill(QtCore.Qt.transparent)
            p = QtGui.QPixmap(paths).scaled(
                56, 56, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)

            painter = QtGui.QPainter(self.target)
            painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
            painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing, True)
            painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)

            path = QtGui.QPainterPath()
            path.addRoundedRect(0, 0, 56, 56, 28, 28)

            painter.setClipPath(path)
            painter.drawPixmap(0, 0, p)
            self.ui.button_profile.setIcon(self.target)

        # a method to resize any picked image from the user and resizes it to 300x300
        def image_resize(picname: str):
            image = cv2.imread(picname)

            width = 300
            height = 300
            dimension = (width, height)

            resized_img = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)

            cv2.imwrite(f'{picname}', resized_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # the method to open the dialog box to choose the profile picture. uses tkinter to get the file path
        def image_open():
            root = Tk()
            root.filename = filedialog.askopenfilename(initialdir='/', title='Choose your profile picture',
                                                       filetypes=(('Picture Files', '*.png *.jpg *.jpeg *.bmp *.dib'),
                                                                  ('PNG Files', '*.png'),
                                                                  ('JPG Files', '*.jpg *.jpeg'),
                                                                  ('BMP Files', '*.bmp *.dib')))
            root.title('Choose your profile picture')
            path = str(root.filename).replace('/', r'\\')
            root.destroy()
            return path

        # the method to set the image picked by the user as their profile picture, and as a initial method to
        # set the user pc profile image as their app profile image on Wolf
        def user_folder(path, name=f'{socket.gethostname()}'):
            # if user cancels the image selection, this method is passed to prevent any data loss and or program error,
            # defined by the 'if' statement below
            if path == '':
                pass

            else:
                # try to do the stuff below. change os dir > make user folder > copy from user image selection and or
                # from user's Windows profile picture > set it to the button icon and user's profile picture on user
                # profile page
                try:
                    # listing the user folders and appending it to the 'usernames' list
                    os.chdir(destination_path)
                    usernames = []
                    for names in os.listdir(destination_path):
                        usernames.append(names)

                    # if the user folder on Wolf already exist then do the if statement, else create a new folder
                    if name in usernames:

                        # if the user if a rascal (trying to break the program), this if statement below will
                        # prevent it, since the rest of the file is to copy the file from the path picked by the user,
                        # remove the image from the Wolf user folder, paste the file, then finally applying the changes
                        if path == image_change_path:
                            return round_avatar_icon(image_change_path), round_avatar(image_change_path)

                        # change dir
                        os.chdir(f'{destination_path}\\{name}')

                        # below until the next comment is the attempt to remove the image file from the Wolf user folder
                        files = ''
                        for i in os.listdir(f'{destination_path}\\{name}'):
                            files += f'{i} '
                        images = re.findall(r'\.png|\.jpg|\.jpeg|\.PNG|\.JPG|\.JPEG|\.bmp|\.BMP', files)
                        for i in images: files = i
                        os.remove(f'{name}{files}')

                        # path to copy the file, preserving the original file for later purposes
                        copyfile_path = path

                        # replacing the '\\' to nothing since it'll look something like this:
                        # \\image_name.image_extension
                        new_path = copyfile_path[copyfile_path.rfind('\\'):].replace('\\', '')

                        # copy the file from the picked path
                        shutil.copy(copyfile_path, f'{destination_path}\\{name}')

                        # resize the image to 300 x 300
                        image_resize(f'{destination_path}\\{name}\\{new_path}')

                        # rename the file to pc name
                        os.rename(f'{destination_path}\\{name}\\{new_path}',
                                  f'{name}{copyfile_path[copyfile_path.rfind("."):]}')

                        # calling the round_avatar_icon to set the user profile button icon and round_avatar to set
                        # the user profile image on the user profile page
                        return round_avatar_icon(
                            f'{destination_path}\\{name}\\{name}{copyfile_path[copyfile_path.rfind("."):]}'), round_avatar(
                            f'{destination_path}\\{name}\\{name}{copyfile_path[copyfile_path.rfind("."):]}')

                    else:
                        # similar thing happen on this else statement, as in the if statement above
                        # preserving the original path
                        copyfile_path = path

                        # replacing the double backslash with nothing
                        new_path = copyfile_path[copyfile_path.rfind('\\'):].replace('\\', '')

                        # making a new directory based on the pc name
                        os.makedirs(name)

                        # copy the file from the original path to the new path (which is the Wolf user folder)
                        shutil.copy(copyfile_path, f'{destination_path}\\{name}')

                        # resize the image
                        image_resize(f'{destination_path}\\{name}\\{new_path}')

                        # change dir to Wolf user folder
                        os.chdir(f'{destination_path}\\{name}')

                        # rename the copied file
                        os.rename(f'{destination_path}\\{name}\\{new_path}',
                                  f'{name}{copyfile_path[copyfile_path.rfind("."):]}')

                        # calling the function to set the user page button icon and user profile image
                        return round_avatar_icon(
                            f'{destination_path}\\{name}\\{name}{copyfile_path[copyfile_path.rfind("."):]}'), round_avatar(
                            f'{destination_path}\\{name}\\{name}{copyfile_path[copyfile_path.rfind("."):]}')

                # if any error(s) happened during the process it'll revert changes by deleting the user folder
                # (if it is the first time the folder is created. else it'll just pass)
                except:
                    shutil.rmtree(f'{destination_path}\\{name}', ignore_errors=True)

        # register a new user or update the existing user profile if the username already exist
        def register():
            test = image_open()
            user_folder(test)

        # method to read the user configuration file (the .json file in the Wolf user folder)
        def read_config():
            # globalling these variables so it can be accessed by other methods
            global stylesheet
            global name
            global tip

            # initializing the variable config_file to check whether the config.json exist or not
            config_file = False

            # change dir to Wolf user folder
            os.chdir(f'{destination_path}\\{socket.gethostname()}')

            # listing the dir and searching the config.json. if found then config_file = True
            for config in os.listdir():
                if config == 'config.json':
                    config_file = True
                    break

            # if config file exist then open it and update the user_config dict and also the self
            # variables to overwrite the default values, else pass and the default values are
            # unchanged
            if config_file == True:
                with open('config.json', 'r+', encoding='utf-8') as file:
                    file = file.read()
                file2 = eval(file)
                self.stylesheet = file2['stylesheet']
                self.name = file2['name']
                self.tip = file2['tip']
                stylesheet = file2['stylesheet']
                name = file2['name']
                tip = file2['tip']
                user_config.update({'stylesheet': file2['stylesheet']})
                user_config.update({'name': file2['name']})
                user_config.update({'tip': file2['tip']})
                set_style(self.stylesheet)
                if tip == 'False':
                    hide_tips()
                elif tip == 'True':
                    show_tips()
                self.ui.user_name.setText(self.name)
                print(user_config)
            else:
                pass

        # method which include Wolf's voice.
        def assistant(self):
            # hiding the welcome text
            self.ui.init.hide()

            # executing the voice input recognizer function. read explanation on assistant library
            voice_input = assist.voice_input()

            # if return value is error then set user input text on GUI to that, and set the result
            # text on GUI to that
            if voice_input[-1] == 'error':
                self.ui.user_input.setText('')
                self.ui.result.setText(f'Sorry, I didn\'t get that. Please try again')
                assist.voice(f'Sorry, I didn\'t get that. Please try again')
                pass

            # elif return value is maintenance, same as above but with different result
            elif voice_input[-1] == 'maintenance':
                self.ui.result.setText(f'Sorry, my voice recognition service is under maintenance right now.'
                                       f'You can instead type your query on the command bar below.')
                assist.voice(f'Sorry, my voice recognition service is under maintenance.')
                pass

            # elif return value is error, show the welcome text
            elif voice_input[-1] == 'none':
                self.ui.init.show()

            else:
                # elif return value is play then set the text to that and try to search on youtube or yt music. after
                # the link has been found then open that video on new tab browser and play the music/video
                if voice_input[-1] == 'play':
                    self.ui.user_input.setText(f'search and play "{voice_input[0]}" on {voice_input[1]}')
                    asis = assist.output(f'search and play "{voice_input[0]}" on {voice_input[1]}')

                # elif return value is search then set the user input text on GUI to that and perform the search
                # attempt on assist.output(input) function. explanation on assistant library
                elif voice_input[-1] == 'search':
                    self.ui.user_input.setText(f'search "{voice_input[0]} on {voice_input[1]}"')
                    asis = assist.output(f'search "{voice_input[0]}" on {voice_input[1]}')

                # elif return value is note then make a new note, other note functions such as view and delete don't
                # need input, only make requires the user input, that's why the other two isn't here
                elif voice_input[-1] == 'note':
                    self.ui.user_input.setText(f'make a new note "{voice_input[0]}"')
                    asis = assist.output(f'make a new note "{voice_input[0]}"')

                # elif return value is screenshot then perform a screenshot. the main idea here is to minimize
                # the GUI then perform the screenshot, but it'll freeze the GUI it'll fail to minimize.
                # this is why I use threading here, and somehow it works while the alarm function doesn't ;w;
                elif voice_input[-1] == 'screenshot':
                    self.ui.user_input.setText(f'{voice_input[0]}')
                    asis = screenshot.main()
                    shot_voice(asis)

                # else if the return value isn't defined above, it'll go to the else function below and perform the
                # command using the assist.output(input) function.
                else:
                    self.ui.user_input.setText(voice_input[0])
                    asis = assist.output(voice_input[0])

                # after everything above is done, it'll go to this try state below and check the return value
                try:
                    # if index 2 of return value is a list then it's definitely a weather. no other return values are
                    # list-type. it'll set the GUI to show the current weather of the city the user asked Wolf to
                    # display the info
                    if type(asis[-1]) == list:
                        self.ui.search.hide()
                        self.ui.weather.show()
                        self.ui.city.setText(f'{asis[-1][0]}, {asis[-1][1]}')
                        self.ui.country.setText(time.strftime('%A, %d %B %Y'))
                        self.ui.weather_icon.setPixmap(f'C:/Wolf/images/icons/weather/{asis[-1][4]}')
                        self.ui.visibility.setText(f'Visibility: {asis[-1][-4][:-3]}.{asis[-1][-4][1]} km')
                        self.ui.pressure.setText(f'Pressure: {asis[-1][-3]} hPa')
                        self.ui.humidity.setText(f'Humidity: {asis[-1][-5]}%')
                        self.ui.high_low.setText(f'Feels like {asis[-1][-2]}°C. {asis[-1][-1]}')
                        self.ui.temp.setText(f'{asis[-1][2]}°')
                        self.ui.weathercond.setText(asis[-1][5])

                    # else if it's not a list then set the result text to the return value of the command attempt
                    else:
                        self.ui.weather.hide()
                        self.ui.search.show()

                        # try to set the text on the 2nd index of return value as the result text, if error then
                        # goes to the exception underneath it
                        try:
                            self.ui.result.setText(asis[-1])
                        except:
                            self.ui.result.setText(asis[-1][-1])

                # if error(s) happened during any of above process, it'll abort and instead show the welcome screen
                except:
                    self.ui.init.show()
                    self.ui.search.hide()
                    self.ui.weather.hide()

        # method that won't be using Wolf's voice
        def assistant_novoice(self):
            self.ui.init.hide()
            asis = langsung.output(self.ui.commandbar.text().lower())
            print(asis)
            try:
                # if the return value is a list, then it's a weather. definitely.
                if type(asis[-1]) == list:
                    self.ui.search.hide()
                    self.ui.weather.show()
                    self.ui.city.setText(f'{asis[-1][0]}, {asis[-1][1]}')
                    self.ui.country.setText(time.strftime('%A, %d %B %Y'))
                    self.ui.weather_icon.setPixmap(f'C:/Wolf/images/icons/weather/{asis[-1][4]}')
                    self.ui.visibility.setText(f'Visibility: {asis[-1][-4][:-3]}.{asis[-1][-4][1]} km')
                    self.ui.pressure.setText(f'Pressure: {asis[-1][-3]} hPa')
                    self.ui.humidity.setText(f'Humidity: {asis[-1][-5]}%')
                    self.ui.high_low.setText(f'Feels like {asis[-1][-2]}°C. {asis[-1][-1]}')
                    self.ui.temp.setText(f'{asis[-1][2]}°')
                    self.ui.weathercond.setText(asis[-1][5])

                # elif the return value is a string, it'll execute the else statement below
                else:
                    self.ui.weather.hide()
                    self.ui.search.show()
                    self.ui.user_input.setText(self.ui.commandbar.text())
                    self.ui.result.setText(asis[-1])

            # if error(s) happened then it'll abort everything and set the GUI to the welcome screen
            except:
                greeting()
                self.ui.search.hide()
                self.ui.weather.hide()

        # method to show the change_name bar when the edit button is clicked
        def change_name():
            self.ui.user_name.hide()
            self.ui.button_edit_name.hide()
            self.ui.change_name.show()
            self.ui.button_confirm_changename.show()

        # method to confirm the name changes made by user. if it's empty it'll pass,
        # if not then it'll set the name to anything inputted by the user.
        def confirm_name():
            global name
            self.ui.user_name.show()
            self.ui.button_edit_name.show()
            self.ui.change_name.hide()
            self.ui.button_confirm_changename.hide()
            if self.ui.change_name.text() == '':
                pass
            else:
                self.ui.change_name.text().strip()
                self.ui.user_name.setText(self.ui.change_name.text())
                self.name = self.ui.change_name.text()
                name = self.ui.change_name.text()
                greeting()
                save_config(stylesheet=self.stylesheet, name=self.name, tip=self.tip)
                self.ui.change_name.setText('')
                self.ui.search.hide()
                self.ui.weather.hide()
                print(self.name)

        # method to hide the tips on the user profile page.
        # yes, these below is only to show the tips
        def hide_tips():
            global tip
            self.ui.button_show_tips.show()
            self.ui.button_hide_tips.hide()
            self.ui.tip_1_up.hide()
            self.ui.tip_2_bottom.hide()
            self.ui.tip_3_bottomright.hide()
            self.ui.tip_4_buttomleft.hide()
            self.ui.arrow_downleft.hide()
            self.ui.arrow_serongkanan.hide()
            self.ui.arrow_upleft.hide()
            self.ui.arrow_upright.hide()
            self.tip = False
            tip = self.tip
            print(self.tip)

        # method to show the tips on the user profile page
        def show_tips():
            global tip
            self.ui.button_show_tips.hide()
            self.ui.button_hide_tips.show()
            self.ui.tip_1_up.show()
            self.ui.tip_2_bottom.show()
            self.ui.tip_3_bottomright.show()
            self.ui.tip_4_buttomleft.show()
            self.ui.arrow_downleft.show()
            self.ui.arrow_serongkanan.show()
            self.ui.arrow_upleft.show()
            self.ui.arrow_upright.show()
            self.tip = True
            tip = self.tip
            print(self.tip)

        # initialize on every launch to set the user picture
        def first_launch():
            global image_change_path

            # if this project is cloned to other pc with different name, it'll be many users, hence a list is needed
            # to check whether the pc this project is currently in already has a Wolf user folder or not. if not then
            # create a new folder based on pc's name
            users = []
            os.chdir(destination_path)
            for user in os.listdir():
                users.append(user)
            if socket.gethostname() in users:
                files = ''
                for file in os.listdir(
                        f'{destination_path}\\{socket.gethostname()}'):  # equivalent to C:/Wolf/users/(yourpcname)
                    files += f'{file} '  # appending the files into a string for the regex to find

                # regex to find the image file extension
                images = re.findall(r'\.png|\.jpg|\.jpeg|\.PNG|\.JPG|\.JPEG|\.bmp|\.BMP', files)

                # loops again to finally get the image file extension
                for image in images:
                    files = image

                # the dir change path to find the image
                image_change_path = f'{socket.gethostname()}{files}'

                # equivalent to C:/Wolf/users/(your_pc_name)/(your_pc_name.image_file_extension)
                final_image = f'{destination_path}\\{socket.gethostname()}\\{socket.gethostname()}{files}'

                # return and call the round_avatar function to set the user profile picture on the user config page,
                # also call round_avatar_icon to set the user configuration button on the top right
                return round_avatar(final_image), round_avatar_icon(final_image)

            else:
                # calling the init library to set the profile image. read the explanation there
                first_open = init.main()
                user_folder(path=f'C:\\Wolf\\images\\convert\\{first_open}')
                print(first_open)

        # method to save user configurations, as explained in the comment below (atexit comment)
        def save_config(stylesheet: str, name: str, tip: bool):
            # these prints functions are just for debugging only, doesn't have
            # any relations to the main function
            print(stylesheet)
            print(name)
            print(tip)

            # if config_file == False will open the user configuration and set the theme
            # to user's saved theme
            config_file = False
            os.chdir(f'{destination_path}\\{socket.gethostname()}')
            for config in os.listdir():
                if config == 'config.json':
                    config_file = True
                    break
                else:
                    pass

            # if config file exist then open it and update the user_config dict
            if config_file == True:
                file = open('config.json', 'w+', encoding='utf-8')
                user_config.update({'stylesheet': f'{self.stylesheet}'})
                user_config.update({'name': f'{self.name}'})
                user_config.update({'tip': f'{self.tip}'})
                file.write(f'{user_config}')
                file.close()

            # else it'll set all by default settings
            else:
                user_config.update({'stylesheet': f'{self.stylesheet}'})
                user_config.update({'name': f'{self.name}'})
                user_config.update({'tip': f'{self.tip}'})
                file = open('config.json', 'w+', encoding='utf-8')
                file.write(f'{user_config}')
                file.close()
            print(f'Done! Saved user configuration: {self.stylesheet}; {self.name}; {self.tip}')

        # if user hides the tip it'll make self.tip False, otherwise it'll make self.tip True.
        # Both will execute respective functions. show_tips() on line 354 and hide_tips() on line 337
        if self.tip:
            show_tips()
        else:
            hide_tips()

        # when the button is clicked, it will execute the assistant program and
        # at the same time prints what it produce(s) into the console.
        # button_command is the one without assistant voice, and button_speak is otherwise.
        # button_command is present with the search icon on the main window and button_speak
        # is present with the microphone icon on the main window.
        self.ui.button_command.clicked.connect(lambda: assistant_novoice(self))
        self.ui.button_command.clicked.connect(lambda: print(self.ui.commandbar.text()))
        self.ui.button_speak.clicked.connect(lambda: listen_sound_execute())
        self.ui.button_speak.clicked.connect(lambda: assistant(self))

        # summoning a new background process to always listen so Wolf can be called by wake-up words
        child_process_listen = always_listen()
        self.ui.button_close_app.clicked.connect(lambda: kill_child(child_process_listen))

        # hiding the search and weather widget on launch, also the edit name bar
        self.ui.weather.hide()
        self.ui.search.hide()
        self.ui.change_name.hide()
        self.ui.button_confirm_changename.hide()

        # other button functionalities. yeah, i have to define one by one
        self.ui.button_profile.clicked.connect(lambda: self.ui.main_page.setCurrentWidget(self.ui.page_profile))
        self.ui.button_home.clicked.connect(lambda: self.ui.main_page.setCurrentWidget(self.ui.page_home))
        self.ui.button_home.clicked.connect(lambda: confirm_name())
        self.ui.button_show_tips.clicked.connect(lambda: show_tips())
        self.ui.button_hide_tips.clicked.connect(lambda: hide_tips())
        self.ui.button_edit_name.clicked.connect(lambda: change_name())
        self.ui.button_confirm_changename.clicked.connect(lambda: confirm_name())
        self.ui.button_documentation.clicked.connect(lambda: os.startfile('C:/Wolf/images/doc.txt'))
        self.ui.profile_change.clicked.connect(lambda: register())
        self.ui.button_color_atlas.clicked.connect(lambda: set_style('atlas'))
        self.ui.button_color_biruish.clicked.connect(lambda: set_style('biruish'))
        self.ui.button_color_darkknight.clicked.connect(lambda: set_style('darkknight'))
        self.ui.button_color_grayscale.clicked.connect(lambda: set_style('grayscale'))
        self.ui.button_color_hersheys.clicked.connect(lambda: set_style('hersheys'))
        self.ui.button_color_lime.clicked.connect(lambda: set_style('lime'))
        self.ui.button_color_lizard.clicked.connect(lambda: set_style('lizard'))
        self.ui.button_color_nightday.clicked.connect(lambda: set_style('nightday'))
        self.ui.button_color_passion.clicked.connect(lambda: set_style('passion'))
        self.ui.button_color_piglet.clicked.connect(lambda: set_style('piglet'))
        self.ui.button_color_predawn.clicked.connect(lambda: set_style('predawn'))
        self.ui.button_color_purplish.clicked.connect(lambda: set_style('purplish'))
        self.ui.button_color_sagepersuasive.clicked.connect(lambda: set_style('sagepersuasive'))
        self.ui.button_color_sunset.clicked.connect(lambda: set_style('sunset'))
        self.ui.button_color_thestrain.clicked.connect(lambda: set_style('thestrain'))
        self.ui.button_color_timber.clicked.connect(lambda: set_style('timber'))
        self.ui.button_color_tree.clicked.connect(lambda: set_style('tree'))
        self.ui.button_color_turqoise.clicked.connect(lambda: set_style('turqoise'))
        self.ui.button_color_vine.clicked.connect(lambda: set_style('vine'))

        # executing the first_launch method to set the profile picture and showing the window,
        # also removing the title bar and replacing it with the custom one
        first_launch()
        read_config()
        greeting()
        UIFunctions.remove_title(self)

        # this atexit module is used to save the user configurations such as their name, their preferred
        # color theme, and their choice of showing the tips or not
        atexit.register(save_config, stylesheet=self.stylesheet, name=self.name, tip=self.tip)

        # showing the main window and killing the splash screen
        self.show()
        time.sleep(1)
        self.splash.send_signal(signal.CTRL_BREAK_EVENT)

    # since this program uses custom title bar, it is necessary for below method to be used in order
    # for the window to be moved when the left mouse is pressed and drags the title bar. Apparently
    # I can't change the method name to whatever I like because this method will be used by the main
    # PySide2(PyQt5) module.
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


# running the program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
