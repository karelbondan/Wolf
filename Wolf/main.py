# Base by Wanderson M. Pimenta
# Mass-modification by Karel Bondan
# Project made with: Qt Designer and PySide2

import sys
import platform
import PyQt5
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
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

# GUI file, includes the main interface template, which of course I made myself using the
# PySide2 Designer program  came together with the installed module.
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


# the main user interface class
class MainWindow(QMainWindow):
    # initial constructor
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.user_name.setText(socket.gethostname())
        self.counter = 0
        self.stylesheet = 'turqoise'
        self.name = socket.gethostname()
        self.tip = True

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

        def move_window(event):
            # moves the windows if the left mouse button is pressed
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_appcontrol.mouseMoveEvent = move_window

        # a method to set the stylsheet when user presses the button.
        def set_style(stylename):
            global stylesheet
            self.ui.all_content.setStyleSheet(background_colors[stylename])
            self.stylesheet = stylename
            stylesheet = self.stylesheet
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

        # the method to open the dialog box to choose the profile picture
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

        # the method to set the image picked by the user as their profile picture
        def user_folder(path, name=f'{socket.gethostname()}'):
            # if user cancels the image selection, this method is passed to prevent any data loss and or program error,
            # defined by the 'if' statement below
            if path == '':
                pass
            else:

                # try to do the stuff below. change os dir > make user folder > copy from user image selection and or
                # from user's Windows profile picture > set it to the button icon and user's profile picture on user
                # config page
                try:
                    os.chdir(destination_path)
                    usernames = []
                    for names in os.listdir(destination_path):
                        usernames.append(names)
                    if name in usernames:
                        if path == image_change_path:
                            return round_avatar_icon(image_change_path), round_avatar(image_change_path)
                        os.chdir(f'{destination_path}\\{name}')
                        files = ''
                        for i in os.listdir(f'{destination_path}\\{name}'):
                            files += f'{i} '
                        images = re.findall(r'\.png|\.jpg|\.jpeg|\.PNG|\.JPG|\.JPEG|\.bmp|\.BMP', files)
                        for i in images: files = i
                        os.remove(f'{name}{files}')
                        copyfile_path = path
                        new_path = copyfile_path[copyfile_path.rfind('\\'):].replace('\\', '')
                        shutil.copy(copyfile_path, f'{destination_path}\\{name}')
                        image_resize(f'{destination_path}\\{name}\\{new_path}')
                        os.rename(f'{destination_path}\\{name}\\{new_path}',
                                  f'{name}{copyfile_path[copyfile_path.rfind("."):]}')
                        round_avatar(f'{destination_path}\\{name}\\{name}{copyfile_path[copyfile_path.rfind("."):]}')
                        return round_avatar_icon(
                            f'{destination_path}\\{name}\\{name}{copyfile_path[copyfile_path.rfind("."):]}'), round_avatar(
                            f'{destination_path}\\{name}\\{name}{copyfile_path[copyfile_path.rfind("."):]}')
                    else:
                        copyfile_path = path
                        new_path = copyfile_path[copyfile_path.rfind('\\'):].replace('\\', '')
                        os.makedirs(name)
                        shutil.copy(copyfile_path, f'{destination_path}\\{name}')
                        image_resize(f'{destination_path}\\{name}\\{new_path}')
                        os.chdir(f'{destination_path}\\{name}')
                        os.rename(f'{destination_path}\\{name}\\{new_path}',
                                  f'{name}{copyfile_path[copyfile_path.rfind("."):]}')
                        round_avatar(f'{destination_path}\\{name}\\{name}{copyfile_path[copyfile_path.rfind("."):]}')
                        return round_avatar_icon(
                            f'{destination_path}\\{name}\\{name}{copyfile_path[copyfile_path.rfind("."):]}'), round_avatar(
                            f'{destination_path}\\{name}\\{name}{copyfile_path[copyfile_path.rfind("."):]}')
                except:
                    shutil.rmtree(f'{destination_path}\\{name}', ignore_errors=True)

        # register a new user or update the existing user profile if the username already exist
        def register():
            test = image_open()
            user_folder(test)

        def read_config():
            global stylesheet
            global name
            global tip
            config_file = False
            os.chdir(f'{destination_path}\\{socket.gethostname()}')
            for config in os.listdir():
                if config == 'config.json':
                    config_file = True
                    break

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

        def assistant(self):
            self.ui.init.hide()
            asis = assist.output(self.ui.commandbar.text().lower())
            print(asis)
            try:
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
                else:
                    self.ui.weather.hide()
                    self.ui.search.show()
                    self.ui.user_input.setText(self.ui.commandbar.text())
                    self.ui.result.setText(asis[-1])
            except:
                self.ui.init.show()
                self.ui.search.hide()
                self.ui.weather.hide()

        def assistant_novoice(self):
            self.ui.init.hide()
            asis = langsung.output(self.ui.commandbar.text().lower())
            print(asis)
            try:
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
                else:
                    self.ui.weather.hide()
                    self.ui.search.show()
                    self.ui.user_input.setText(self.ui.commandbar.text())
                    self.ui.result.setText(asis[-1])
            except:
                greeting()
                self.ui.search.hide()
                self.ui.weather.hide()

        def change_name():
            self.ui.user_name.hide()
            self.ui.button_edit_name.hide()
            self.ui.change_name.show()
            self.ui.button_confirm_changename.show()

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

        # initialize when first open
        def first_launch():
            global image_change_path
            users = []
            os.chdir(destination_path)
            for user in os.listdir():
                users.append(user)
            if socket.gethostname() in users:
                files = ''
                for file in os.listdir(f'{destination_path}\\{socket.gethostname()}'):
                    files += f'{file} '
                images = re.findall(r'\.png|\.jpg|\.jpeg|\.PNG|\.JPG|\.JPEG|\.bmp|\.BMP', files)
                for image in images:
                    files = image
                image_change_path = f'{socket.gethostname()}{files}'
                final_image = f'{destination_path}\\{socket.gethostname()}\\{socket.gethostname()}{files}'

                # return and call the round_avatar function to set the user profile picture on the user config page,
                # also call round_avatar_icon to set the user configuration button on the top right
                return round_avatar(final_image), round_avatar_icon(final_image)
            else:
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

            if config_file == True:
                file = open('config.json', 'w+', encoding='utf-8')
                user_config.update({'stylesheet': f'{self.stylesheet}'})
                user_config.update({'name': f'{self.name}'})
                user_config.update({'tip': f'{self.tip}'})
                file.write(f'{user_config}')
                file.close()

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
        self.ui.button_speak.clicked.connect(lambda: assistant(self))
        self.ui.button_speak.clicked.connect(lambda: print('mic button pressed.'))

        # hiding the search and weather widget on launch, also the edit name bar
        self.ui.weather.hide()
        self.ui.search.hide()
        self.ui.change_name.hide()
        self.ui.button_confirm_changename.hide()

        # other button functionalities
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

        # showing the main window
        self.show()

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
