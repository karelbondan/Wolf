# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assistant_finalxFSrUV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(930, 885)
        MainWindow.setMinimumSize(QSize(930, 885))
        MainWindow.setMaximumSize(QSize(930, 885))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.all_content = QFrame(self.centralwidget)
        self.all_content.setObjectName(u"all_content")
        self.all_content.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.455, x2:1, y2:0.733, stop:0 rgba(19, 106, 138, 255), stop:1 rgba(38, 120, 113, 255));")
        self.all_content.setFrameShape(QFrame.StyledPanel)
        self.all_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.all_content)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_appcontrol = QFrame(self.all_content)
        self.frame_appcontrol.setObjectName(u"frame_appcontrol")
        self.frame_appcontrol.setMinimumSize(QSize(0, 25))
        self.frame_appcontrol.setMaximumSize(QSize(16777215, 25))
        self.frame_appcontrol.setStyleSheet(u"background-color: rgba(30, 30, 30, 30);")
        self.frame_appcontrol.setFrameShape(QFrame.StyledPanel)
        self.frame_appcontrol.setFrameShadow(QFrame.Raised)
        self.frame_placeholder_2 = QFrame(self.frame_appcontrol)
        self.frame_placeholder_2.setObjectName(u"frame_placeholder_2")
        self.frame_placeholder_2.setGeometry(QRect(-13, 0, 846, 26))
        self.frame_placeholder_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_placeholder_2.setFrameShape(QFrame.StyledPanel)
        self.frame_placeholder_2.setFrameShadow(QFrame.Raised)
        self.button_minimize_app = QPushButton(self.frame_appcontrol)
        self.button_minimize_app.setObjectName(u"button_minimize_app")
        self.button_minimize_app.setGeometry(QRect(851, 0, 30, 25))
        self.button_minimize_app.setMinimumSize(QSize(30, 25))
        self.button_minimize_app.setMaximumSize(QSize(30, 25))
        self.button_minimize_app.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255, 150);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 1px\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(255, 255, 255, 200);\n"
"	background-color: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	color: rgb(255, 255, 255, 200);\n"
"	background-color: rgba(255, 255, 255, 35);\n"
"}")
        icon = QIcon()
        icon.addFile(u"C:/Wolf/images/icons/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_minimize_app.setIcon(icon)
        self.button_minimize_app.setIconSize(QSize(13, 13))
        self.button_close_app = QPushButton(self.frame_appcontrol)
        self.button_close_app.setObjectName(u"button_close_app")
        self.button_close_app.setGeometry(QRect(881, 0, 30, 25))
        self.button_close_app.setMinimumSize(QSize(30, 25))
        self.button_close_app.setMaximumSize(QSize(30, 25))
        self.button_close_app.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255, 150);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 1px\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(255, 255, 255, 200);\n"
"	background-color: rgb(232, 40, 50);\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"C:/Wolf/images/icons/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_close_app.setIcon(icon1)
        self.button_close_app.setIconSize(QSize(13, 13))

        self.verticalLayout.addWidget(self.frame_appcontrol)

        self.frame_header = QFrame(self.all_content)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMinimumSize(QSize(0, 120))
        self.frame_header.setMaximumSize(QSize(16777215, 120))
        self.frame_header.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_home = QFrame(self.frame_header)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setMinimumSize(QSize(130, 90))
        self.frame_home.setMaximumSize(QSize(130, 100))
        self.frame_home.setFrameShape(QFrame.StyledPanel)
        self.frame_home.setFrameShadow(QFrame.Raised)
        self.button_home = QPushButton(self.frame_home)
        self.button_home.setObjectName(u"button_home")
        self.button_home.setGeometry(QRect(35, 20, 60, 60))
        self.button_home.setMinimumSize(QSize(60, 60))
        self.button_home.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid rgb(125, 125, 125);\n"
"	border-radius: 30px;\n"
"	background-color: rgba(30, 30, 30, 70);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(213, 213, 213);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(30, 30, 30, 80);\n"
"	border: 3px solid rgb(240,240,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(30, 30, 30, 130);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(35, 35, 35);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"C:/Wolf/images/icons/home icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_home.setIcon(icon2)
        self.button_home.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.frame_home)

        self.frame_placeholder = QFrame(self.frame_header)
        self.frame_placeholder.setObjectName(u"frame_placeholder")
        self.frame_placeholder.setMinimumSize(QSize(580, 100))
        self.frame_placeholder.setMaximumSize(QSize(580, 100))
        self.frame_placeholder.setFrameShape(QFrame.StyledPanel)
        self.frame_placeholder.setFrameShadow(QFrame.Raised)
        self.logo = QLabel(self.frame_placeholder)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(230, 0, 91, 91))
        self.logo.setStyleSheet(u"font: 58pt \"ReklameScript-Medium\";\n"
"font: 58pt \"ReklameScript-Regular\";\n"
"color: rgb(255, 255, 255);")
        self.logo.setAlignment(Qt.AlignCenter)
        self.underline = QLabel(self.frame_placeholder)
        self.underline.setObjectName(u"underline")
        self.underline.setGeometry(QRect(140, 70, 311, 31))
        self.underline.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.underline.setAlignment(Qt.AlignCenter)
        self.logo_2 = QLabel(self.frame_placeholder)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setGeometry(QRect(280, 15, 81, 69))
        self.logo_2.setStyleSheet(u"font: 38pt \"ReklameScript-Medium\";\n"
"color: rgb(255, 255, 255);")
        self.logo_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.frame_placeholder)

        self.frame_profile = QFrame(self.frame_header)
        self.frame_profile.setObjectName(u"frame_profile")
        self.frame_profile.setMinimumSize(QSize(130, 100))
        self.frame_profile.setMaximumSize(QSize(130, 100))
        self.frame_profile.setFrameShape(QFrame.StyledPanel)
        self.frame_profile.setFrameShadow(QFrame.Raised)
        self.button_profile = QPushButton(self.frame_profile)
        self.button_profile.setObjectName(u"button_profile")
        self.button_profile.setGeometry(QRect(35, 20, 60, 60))
        self.button_profile.setMinimumSize(QSize(60, 60))
        self.button_profile.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 30px;\n"
"border:  2px solid rgb(255, 255, 255);\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../../../../../../PycharmProjects/virtualssignmentproject-testings/arsen.jpg-resized.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_profile.setIcon(icon3)
        self.button_profile.setIconSize(QSize(60, 60))
        self.button_profile.setCheckable(False)

        self.horizontalLayout.addWidget(self.frame_profile)


        self.verticalLayout.addWidget(self.frame_header)

        self.main_page = QStackedWidget(self.all_content)
        self.main_page.setObjectName(u"main_page")
        self.main_page.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_2 = QVBoxLayout(self.page_home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_content = QFrame(self.page_home)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.weather = QFrame(self.frame_content)
        self.weather.setObjectName(u"weather")
        self.weather.setGeometry(QRect(130, 0, 611, 571))
        self.weather.setFrameShape(QFrame.StyledPanel)
        self.weather.setFrameShadow(QFrame.Raised)
        self.weathercond = QLabel(self.weather)
        self.weathercond.setObjectName(u"weathercond")
        self.weathercond.setGeometry(QRect(240, 400, 161, 41))
        self.weathercond.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 28pt \"SF Pro Display\";")
        self.weathercond.setAlignment(Qt.AlignCenter)
        self.weather_icon = QLabel(self.weather)
        self.weather_icon.setObjectName(u"weather_icon")
        self.weather_icon.setGeometry(QRect(260, 290, 121, 100))
        self.weather_icon.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.weather_icon.setPixmap(QPixmap(u"../../../../../../PycharmProjects/pythonProjecttest/images/weather/04d.png"))
        self.weather_icon.setAlignment(Qt.AlignCenter)
        self.high_low = QLabel(self.weather)
        self.high_low.setObjectName(u"high_low")
        self.high_low.setGeometry(QRect(147, 425, 341, 61))
        self.high_low.setStyleSheet(u"font: 25 18pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")
        self.high_low.setAlignment(Qt.AlignCenter)
        self.city = QLabel(self.weather)
        self.city.setObjectName(u"city")
        self.city.setGeometry(QRect(55, -10, 541, 101))
        self.city.setStyleSheet(u"font: 0 28pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.city.setAlignment(Qt.AlignCenter)
        self.temp = QLabel(self.weather)
        self.temp.setObjectName(u"temp")
        self.temp.setGeometry(QRect(200, 120, 271, 151))
        self.temp.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 0 102pt \"SF Pro Display\";\n"
"")
        self.temp.setAlignment(Qt.AlignCenter)
        self.country = QLabel(self.weather)
        self.country.setObjectName(u"country")
        self.country.setGeometry(QRect(66, 40, 521, 90))
        self.country.setStyleSheet(u"font: 75 14pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")
        self.country.setAlignment(Qt.AlignCenter)
        self.humidity = QLabel(self.weather)
        self.humidity.setObjectName(u"humidity")
        self.humidity.setGeometry(QRect(227, 470, 191, 61))
        self.humidity.setStyleSheet(u"font: 25 12pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")
        self.humidity.setAlignment(Qt.AlignCenter)
        self.visibility = QLabel(self.weather)
        self.visibility.setObjectName(u"visibility")
        self.visibility.setGeometry(QRect(227, 490, 191, 61))
        self.visibility.setStyleSheet(u"font: 25 12pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")
        self.visibility.setAlignment(Qt.AlignCenter)
        self.pressure = QLabel(self.weather)
        self.pressure.setObjectName(u"pressure")
        self.pressure.setGeometry(QRect(227, 510, 191, 61))
        self.pressure.setStyleSheet(u"font: 25 12pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")
        self.pressure.setAlignment(Qt.AlignCenter)
        self.search = QFrame(self.frame_content)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(11, -1, 861, 571))
        self.search.setFrameShape(QFrame.StyledPanel)
        self.search.setFrameShadow(QFrame.Raised)
        self.user_input = QLabel(self.search)
        self.user_input.setObjectName(u"user_input")
        self.user_input.setGeometry(QRect(320, 10, 441, 191))
        self.user_input.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 25 20pt \"SF Pro Display\";")
        self.user_input.setTextFormat(Qt.AutoText)
        self.user_input.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.user_input.setWordWrap(True)
        self.result = QLabel(self.search)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(130, 260, 531, 261))
        self.result.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 0 20pt \"SF Pro Display\";")
        self.result.setTextFormat(Qt.AutoText)
        self.result.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.result.setWordWrap(True)
        self.init = QLabel(self.frame_content)
        self.init.setObjectName(u"init")
        self.init.setGeometry(QRect(120, 180, 671, 181))
        self.init.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgba(255, 255, 255, 100);\n"
"font: 0 30pt \"SF Pro Display\";")
        self.init.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.frame_content)

        self.frame_command = QFrame(self.page_home)
        self.frame_command.setObjectName(u"frame_command")
        self.frame_command.setMinimumSize(QSize(0, 100))
        self.frame_command.setMaximumSize(QSize(16777215, 110))
        self.frame_command.setFrameShape(QFrame.StyledPanel)
        self.frame_command.setFrameShadow(QFrame.Raised)
        self.commandbar = QLineEdit(self.frame_command)
        self.commandbar.setObjectName(u"commandbar")
        self.commandbar.setGeometry(QRect(130, 30, 471, 60))
        self.commandbar.setMaximumSize(QSize(16777215, 60))
        self.commandbar.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	border-radius: 30px;\n"
"	padding: 15px;\n"
"	background-color: rgba(30, 30, 30, 70);\n"
"	color: rgb(213, 213, 213);\n"
"	font: 87 12pt \"SF Pro Display\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(240,240,240);\n"
"	padding: 14px;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 255, 255);\n"
"	padding: 14px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.button_speak = QPushButton(self.frame_command)
        self.button_speak.setObjectName(u"button_speak")
        self.button_speak.setGeometry(QRect(640, 30, 60, 60))
        self.button_speak.setMaximumSize(QSize(60, 60))
        self.button_speak.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid rgb(125, 125, 125);\n"
"	border-radius: 30px;\n"
"	background-color: rgba(30, 30, 30, 70);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(213, 213, 213);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(30, 30, 30, 80);\n"
"	border: 3px solid rgb(240,240,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(30, 30, 30, 130);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(35, 35, 35);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"C:/Wolf/images/icons/mic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_speak.setIcon(icon4)
        self.button_speak.setIconSize(QSize(40, 40))
        self.button_command = QPushButton(self.frame_command)
        self.button_command.setObjectName(u"button_command")
        self.button_command.setGeometry(QRect(730, 30, 60, 60))
        self.button_command.setMaximumSize(QSize(60, 60))
        self.button_command.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid rgb(125, 125, 125);\n"
"	border-radius: 30px;\n"
"	background-color: rgba(30, 30, 30, 70);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(213, 213, 213);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(30, 30, 30, 80);\n"
"	border: 3px solid rgb(240,240,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(30, 30, 30, 130);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(35, 35, 35);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"C:/Wolf/images/icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_command.setIcon(icon5)
        self.button_command.setIconSize(QSize(35, 35))

        self.verticalLayout_2.addWidget(self.frame_command)

        self.main_page.addWidget(self.page_home)
        self.page_profile = QWidget()
        self.page_profile.setObjectName(u"page_profile")
        self.verticalLayout_3 = QVBoxLayout(self.page_profile)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_settings = QFrame(self.page_profile)
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_settings.setFrameShadow(QFrame.Raised)
        self.user_name = QLabel(self.frame_settings)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setGeometry(QRect(110, 460, 221, 101))
        self.user_name.setStyleSheet(u"font: 25 28pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")
        self.user_name.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.user_name.setWordWrap(True)
        self.arrow_downleft = QLabel(self.frame_settings)
        self.arrow_downleft.setObjectName(u"arrow_downleft")
        self.arrow_downleft.setGeometry(QRect(340, 100, 51, 61))
        self.arrow_downleft.setPixmap(QPixmap(u"C:/Wolf/images/icons/arrow.png"))
        self.tip_1_up = QLabel(self.frame_settings)
        self.tip_1_up.setObjectName(u"tip_1_up")
        self.tip_1_up.setGeometry(QRect(260, 50, 211, 51))
        self.tip_1_up.setStyleSheet(u"font: 25 16pt \"SF Pro Display\";\n"
"font: 75 14pt \"Andy\";\n"
"color: rgb(255, 255, 255);")
        self.tip_1_up.setAlignment(Qt.AlignCenter)
        self.tip_1_up.setWordWrap(True)
        self.profile_change = QPushButton(self.frame_settings)
        self.profile_change.setObjectName(u"profile_change")
        self.profile_change.setGeometry(QRect(70, 130, 300, 300))
        self.profile_change.setMinimumSize(QSize(300, 300))
        self.profile_change.setMaximumSize(QSize(300, 300))
        self.profile_change.setStyleSheet(u"border-radius: 150px;\n"
"border:  0px solid rgb(255, 255, 255);")
        icon6 = QIcon()
        icon6.addFile(u"C:/Wolf/images/temp/resized_karel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_change.setIcon(icon6)
        self.profile_change.setIconSize(QSize(300, 300))
        self.chooseyourcolor = QLabel(self.frame_settings)
        self.chooseyourcolor.setObjectName(u"chooseyourcolor")
        self.chooseyourcolor.setGeometry(QRect(580, 50, 221, 51))
        self.chooseyourcolor.setStyleSheet(u"font: 18pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")
        self.chooseyourcolor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.separator_2 = QLabel(self.frame_settings)
        self.separator_2.setObjectName(u"separator_2")
        self.separator_2.setGeometry(QRect(804, 60, 50, 30))
        self.separator_2.setMinimumSize(QSize(50, 0))
        self.separator_2.setMaximumSize(QSize(50, 16777215))
        self.separator_2.setStyleSheet(u"font: 25 26pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")
        self.separator_2.setAlignment(Qt.AlignCenter)
        self.button_color_purplish = QPushButton(self.frame_settings)
        self.button_color_purplish.setObjectName(u"button_color_purplish")
        self.button_color_purplish.setGeometry(QRect(500, 110, 50, 50))
        self.button_color_purplish.setMinimumSize(QSize(50, 50))
        self.button_color_purplish.setMaximumSize(QSize(50, 50))
        self.button_color_purplish.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u"C:/Wolf/images/icons/color_purplish.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_purplish.setIcon(icon7)
        self.button_color_purplish.setIconSize(QSize(50, 50))
        self.button_color_lime = QPushButton(self.frame_settings)
        self.button_color_lime.setObjectName(u"button_color_lime")
        self.button_color_lime.setGeometry(QRect(570, 110, 50, 50))
        self.button_color_lime.setMinimumSize(QSize(50, 50))
        self.button_color_lime.setMaximumSize(QSize(50, 50))
        icon8 = QIcon()
        icon8.addFile(u"C:/Wolf/images/icons/color_lime.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_lime.setIcon(icon8)
        self.button_color_lime.setIconSize(QSize(50, 50))
        self.button_color_tree = QPushButton(self.frame_settings)
        self.button_color_tree.setObjectName(u"button_color_tree")
        self.button_color_tree.setGeometry(QRect(640, 110, 50, 50))
        self.button_color_tree.setMinimumSize(QSize(50, 50))
        self.button_color_tree.setMaximumSize(QSize(50, 50))
        icon9 = QIcon()
        icon9.addFile(u"C:/Wolf/images/icons/color_tree.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_tree.setIcon(icon9)
        self.button_color_tree.setIconSize(QSize(50, 50))
        self.button_color_sunset = QPushButton(self.frame_settings)
        self.button_color_sunset.setObjectName(u"button_color_sunset")
        self.button_color_sunset.setGeometry(QRect(710, 110, 50, 50))
        self.button_color_sunset.setMinimumSize(QSize(50, 50))
        self.button_color_sunset.setMaximumSize(QSize(50, 50))
        icon10 = QIcon()
        icon10.addFile(u"C:/Wolf/images/icons/color_sunset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_sunset.setIcon(icon10)
        self.button_color_sunset.setIconSize(QSize(50, 50))
        self.button_color_piglet = QPushButton(self.frame_settings)
        self.button_color_piglet.setObjectName(u"button_color_piglet")
        self.button_color_piglet.setGeometry(QRect(780, 110, 50, 50))
        self.button_color_piglet.setMinimumSize(QSize(50, 50))
        self.button_color_piglet.setMaximumSize(QSize(50, 50))
        icon11 = QIcon()
        icon11.addFile(u"C:/Wolf/images/icons/color_piglet.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_piglet.setIcon(icon11)
        self.button_color_piglet.setIconSize(QSize(50, 50))
        self.button_color_passion = QPushButton(self.frame_settings)
        self.button_color_passion.setObjectName(u"button_color_passion")
        self.button_color_passion.setGeometry(QRect(500, 180, 50, 50))
        self.button_color_passion.setMinimumSize(QSize(50, 50))
        self.button_color_passion.setMaximumSize(QSize(50, 50))
        icon12 = QIcon()
        icon12.addFile(u"C:/Wolf/images/icons/color_passion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_passion.setIcon(icon12)
        self.button_color_passion.setIconSize(QSize(50, 50))
        self.button_color_nightday = QPushButton(self.frame_settings)
        self.button_color_nightday.setObjectName(u"button_color_nightday")
        self.button_color_nightday.setGeometry(QRect(570, 180, 50, 50))
        self.button_color_nightday.setMinimumSize(QSize(50, 50))
        self.button_color_nightday.setMaximumSize(QSize(50, 50))
        icon13 = QIcon()
        icon13.addFile(u"C:/Wolf/images/icons/color_nightnday.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_nightday.setIcon(icon13)
        self.button_color_nightday.setIconSize(QSize(50, 50))
        self.button_color_biruish = QPushButton(self.frame_settings)
        self.button_color_biruish.setObjectName(u"button_color_biruish")
        self.button_color_biruish.setGeometry(QRect(640, 180, 50, 50))
        self.button_color_biruish.setMinimumSize(QSize(50, 50))
        self.button_color_biruish.setMaximumSize(QSize(50, 50))
        icon14 = QIcon()
        icon14.addFile(u"C:/Wolf/images/icons/color_biruish.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_biruish.setIcon(icon14)
        self.button_color_biruish.setIconSize(QSize(50, 50))
        self.button_color_timber = QPushButton(self.frame_settings)
        self.button_color_timber.setObjectName(u"button_color_timber")
        self.button_color_timber.setGeometry(QRect(710, 180, 50, 50))
        self.button_color_timber.setMinimumSize(QSize(50, 50))
        self.button_color_timber.setMaximumSize(QSize(50, 50))
        icon15 = QIcon()
        icon15.addFile(u"C:/Wolf/images/icons/color_timber.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_timber.setIcon(icon15)
        self.button_color_timber.setIconSize(QSize(50, 50))
        self.button_color_atlas = QPushButton(self.frame_settings)
        self.button_color_atlas.setObjectName(u"button_color_atlas")
        self.button_color_atlas.setGeometry(QRect(780, 180, 50, 50))
        self.button_color_atlas.setMinimumSize(QSize(50, 50))
        self.button_color_atlas.setMaximumSize(QSize(50, 50))
        icon16 = QIcon()
        icon16.addFile(u"C:/Wolf/images/icons/color_atlas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_atlas.setIcon(icon16)
        self.button_color_atlas.setIconSize(QSize(50, 50))
        self.button_color_turqoise = QPushButton(self.frame_settings)
        self.button_color_turqoise.setObjectName(u"button_color_turqoise")
        self.button_color_turqoise.setGeometry(QRect(500, 250, 50, 50))
        self.button_color_turqoise.setMinimumSize(QSize(50, 50))
        self.button_color_turqoise.setMaximumSize(QSize(50, 50))
        icon17 = QIcon()
        icon17.addFile(u"C:/Wolf/images/icons/color_turqoiseflow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_turqoise.setIcon(icon17)
        self.button_color_turqoise.setIconSize(QSize(50, 50))
        self.button_color_lizard = QPushButton(self.frame_settings)
        self.button_color_lizard.setObjectName(u"button_color_lizard")
        self.button_color_lizard.setGeometry(QRect(570, 250, 50, 50))
        self.button_color_lizard.setMinimumSize(QSize(50, 50))
        self.button_color_lizard.setMaximumSize(QSize(50, 50))
        icon18 = QIcon()
        icon18.addFile(u"C:/Wolf/images/icons/color_lizard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_lizard.setIcon(icon18)
        self.button_color_lizard.setIconSize(QSize(50, 50))
        self.button_color_sagepersuasive = QPushButton(self.frame_settings)
        self.button_color_sagepersuasive.setObjectName(u"button_color_sagepersuasive")
        self.button_color_sagepersuasive.setGeometry(QRect(640, 250, 50, 50))
        self.button_color_sagepersuasive.setMinimumSize(QSize(50, 50))
        self.button_color_sagepersuasive.setMaximumSize(QSize(50, 50))
        icon19 = QIcon()
        icon19.addFile(u"C:/Wolf/images/icons/color_sagepersuasive.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_sagepersuasive.setIcon(icon19)
        self.button_color_sagepersuasive.setIconSize(QSize(50, 50))
        self.button_color_predawn = QPushButton(self.frame_settings)
        self.button_color_predawn.setObjectName(u"button_color_predawn")
        self.button_color_predawn.setGeometry(QRect(710, 250, 50, 50))
        self.button_color_predawn.setMinimumSize(QSize(50, 50))
        self.button_color_predawn.setMaximumSize(QSize(50, 50))
        icon20 = QIcon()
        icon20.addFile(u"C:/Wolf/images/icons/color_predawn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_predawn.setIcon(icon20)
        self.button_color_predawn.setIconSize(QSize(50, 50))
        self.button_color_darkknight = QPushButton(self.frame_settings)
        self.button_color_darkknight.setObjectName(u"button_color_darkknight")
        self.button_color_darkknight.setGeometry(QRect(780, 250, 50, 50))
        self.button_color_darkknight.setMinimumSize(QSize(50, 50))
        self.button_color_darkknight.setMaximumSize(QSize(50, 50))
        icon21 = QIcon()
        icon21.addFile(u"C:/Wolf/images/icons/color_darkknight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_darkknight.setIcon(icon21)
        self.button_color_darkknight.setIconSize(QSize(50, 50))
        self.button_color_vine = QPushButton(self.frame_settings)
        self.button_color_vine.setObjectName(u"button_color_vine")
        self.button_color_vine.setGeometry(QRect(536, 320, 50, 50))
        self.button_color_vine.setMinimumSize(QSize(50, 50))
        self.button_color_vine.setMaximumSize(QSize(50, 50))
        icon22 = QIcon()
        icon22.addFile(u"C:/Wolf/images/icons/color_vine.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_vine.setIcon(icon22)
        self.button_color_vine.setIconSize(QSize(50, 50))
        self.button_color_hersheys = QPushButton(self.frame_settings)
        self.button_color_hersheys.setObjectName(u"button_color_hersheys")
        self.button_color_hersheys.setGeometry(QRect(606, 320, 50, 50))
        self.button_color_hersheys.setMinimumSize(QSize(50, 50))
        self.button_color_hersheys.setMaximumSize(QSize(50, 50))
        icon23 = QIcon()
        icon23.addFile(u"C:/Wolf/images/icons/color_hersheys.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_hersheys.setIcon(icon23)
        self.button_color_hersheys.setIconSize(QSize(50, 50))
        self.button_color_thestrain = QPushButton(self.frame_settings)
        self.button_color_thestrain.setObjectName(u"button_color_thestrain")
        self.button_color_thestrain.setGeometry(QRect(676, 320, 50, 50))
        self.button_color_thestrain.setMinimumSize(QSize(50, 50))
        self.button_color_thestrain.setMaximumSize(QSize(50, 50))
        icon24 = QIcon()
        icon24.addFile(u"C:/Wolf/images/icons/color_thestrain.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_thestrain.setIcon(icon24)
        self.button_color_thestrain.setIconSize(QSize(50, 50))
        self.button_color_grayscale = QPushButton(self.frame_settings)
        self.button_color_grayscale.setObjectName(u"button_color_grayscale")
        self.button_color_grayscale.setGeometry(QRect(746, 320, 50, 50))
        self.button_color_grayscale.setMinimumSize(QSize(50, 50))
        self.button_color_grayscale.setMaximumSize(QSize(50, 50))
        icon25 = QIcon()
        icon25.addFile(u"C:/Wolf/images/icons/color_grayscale.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_color_grayscale.setIcon(icon25)
        self.button_color_grayscale.setIconSize(QSize(50, 50))
        self.arrow_upright = QLabel(self.frame_settings)
        self.arrow_upright.setObjectName(u"arrow_upright")
        self.arrow_upright.setGeometry(QRect(480, 340, 51, 61))
        self.arrow_upright.setPixmap(QPixmap(u"C:/Wolf/images/icons/arrow_upright.png"))
        self.tip_2_bottom = QLabel(self.frame_settings)
        self.tip_2_bottom.setObjectName(u"tip_2_bottom")
        self.tip_2_bottom.setGeometry(QRect(370, 400, 220, 51))
        self.tip_2_bottom.setStyleSheet(u"font: 25 16pt \"SF Pro Display\";\n"
"font: 75 14pt \"Andy\";\n"
"color: rgb(255, 255, 255);")
        self.tip_2_bottom.setAlignment(Qt.AlignCenter)
        self.tip_2_bottom.setWordWrap(True)
        self.button_edit_name = QPushButton(self.frame_settings)
        self.button_edit_name.setObjectName(u"button_edit_name")
        self.button_edit_name.setGeometry(QRect(330, 468, 30, 30))
        self.button_edit_name.setStyleSheet(u"QPushButton {	\n"
"	border: 1px solid rgb(125, 125, 125);\n"
"	border-radius: 15px;\n"
"	background-color: rgba(30, 30, 30, 70);\n"
"	border: 1px solid rgb(255,255,255);\n"
"	color: rgb(213, 213, 213);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(30, 30, 30, 80);\n"
"	border: 2px solid rgb(240,240,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(30, 30, 30, 130);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(35, 35, 35);\n"
"}")
        icon26 = QIcon()
        icon26.addFile(u"C:/Wolf/images/icons/pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_edit_name.setIcon(icon26)
        self.change_name = QLineEdit(self.frame_settings)
        self.change_name.setObjectName(u"change_name")
        self.change_name.setGeometry(QRect(90, 458, 261, 50))
        self.change_name.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	border-radius: 25px;\n"
"	padding: 15px;\n"
"	background-color: rgba(30, 30, 30, 70);\n"
"	color: rgb(213, 213, 213);\n"
"	font: 87 12pt \"SF Pro Display\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(240,240,240);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(255, 255, 255);	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.change_name.setMaxLength(20)
        self.button_confirm_changename = QPushButton(self.frame_settings)
        self.button_confirm_changename.setObjectName(u"button_confirm_changename")
        self.button_confirm_changename.setGeometry(QRect(206, 530, 30, 30))
        self.button_confirm_changename.setStyleSheet(u"QPushButton {	\n"
"	border: 1px solid rgb(125, 125, 125);\n"
"	border-radius: 15px;\n"
"	background-color: rgba(30, 30, 30, 70);\n"
"	border: 1px solid rgb(255,255,255);\n"
"	color: rgb(213, 213, 213);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(30, 30, 30, 80);\n"
"	border: 2px solid rgb(240,240,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(30, 30, 30, 130);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(35, 35, 35);\n"
"}")
        icon27 = QIcon()
        icon27.addFile(u"C:/Wolf/images/icons/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_confirm_changename.setIcon(icon27)
        self.addyourownapp = QLabel(self.frame_settings)
        self.addyourownapp.setObjectName(u"addyourownapp")
        self.addyourownapp.setGeometry(QRect(580, 400, 221, 51))
        self.addyourownapp.setStyleSheet(u"font: 18pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")
        self.addyourownapp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.separator_3 = QLabel(self.frame_settings)
        self.separator_3.setObjectName(u"separator_3")
        self.separator_3.setGeometry(QRect(804, 410, 50, 30))
        self.separator_3.setMinimumSize(QSize(50, 0))
        self.separator_3.setMaximumSize(QSize(50, 16777215))
        self.separator_3.setStyleSheet(u"font: 25 26pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")
        self.separator_3.setAlignment(Qt.AlignCenter)
        self.button_documentation = QPushButton(self.frame_settings)
        self.button_documentation.setObjectName(u"button_documentation")
        self.button_documentation.setGeometry(QRect(670, 463, 111, 40))
        self.button_documentation.setStyleSheet(u"QPushButton {	\n"
"	border: 1px solid rgb(125, 125, 125);\n"
"	border-radius: 20px;\n"
"	background-color: rgba(30, 30, 30, 70);\n"
"	border: 1px solid rgb(255,255,255);\n"
"	color: rgb(235, 235, 235);\n"
"	font: 25 10pt \"SF Pro Display\";\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(30, 30, 30, 80);\n"
"	border: 2px solid rgb(240,240,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(30, 30, 30, 130);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(255,255,255);\n"
"}")
        self.arrow_serongkanan = QLabel(self.frame_settings)
        self.arrow_serongkanan.setObjectName(u"arrow_serongkanan")
        self.arrow_serongkanan.setGeometry(QRect(695, 520, 51, 41))
        self.arrow_serongkanan.setPixmap(QPixmap(u"C:/Wolf/images/icons/arrow_up_serongkanan.png"))
        self.tip_3_bottomright = QLabel(self.frame_settings)
        self.tip_3_bottomright.setObjectName(u"tip_3_bottomright")
        self.tip_3_bottomright.setGeometry(QRect(605, 560, 220, 51))
        self.tip_3_bottomright.setStyleSheet(u"font: 25 16pt \"SF Pro Display\";\n"
"font: 75 12pt \"Andy\";\n"
"color: rgb(255, 255, 255);")
        self.tip_3_bottomright.setAlignment(Qt.AlignCenter)
        self.tip_3_bottomright.setWordWrap(True)
        self.arrow_upleft = QLabel(self.frame_settings)
        self.arrow_upleft.setObjectName(u"arrow_upleft")
        self.arrow_upleft.setGeometry(QRect(370, 500, 51, 41))
        self.arrow_upleft.setPixmap(QPixmap(u"C:/Wolf/images/icons/arrow_upleft.png"))
        self.tip_4_buttomleft = QLabel(self.frame_settings)
        self.tip_4_buttomleft.setObjectName(u"tip_4_buttomleft")
        self.tip_4_buttomleft.setGeometry(QRect(270, 550, 220, 51))
        self.tip_4_buttomleft.setStyleSheet(u"font: 25 16pt \"SF Pro Display\";\n"
"font: 75 12pt \"Andy\";\n"
"color: rgb(255, 255, 255);")
        self.tip_4_buttomleft.setAlignment(Qt.AlignCenter)
        self.tip_4_buttomleft.setWordWrap(True)
        self.button_show_tips = QPushButton(self.frame_settings)
        self.button_show_tips.setObjectName(u"button_show_tips")
        self.button_show_tips.setGeometry(QRect(35, 10, 81, 40))
        self.button_show_tips.setStyleSheet(u"QPushButton {	\n"
"	border: 1px solid rgb(125, 125, 125);\n"
"	border-radius: 20px;\n"
"	background-color: rgba(30, 30, 30, 70);\n"
"	border: 1px solid rgb(255,255,255);\n"
"	color: rgb(235, 235, 235);\n"
"	font: 25 10pt \"SF Pro Display\";\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(30, 30, 30, 80);\n"
"	border: 2px solid rgb(240,240,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(30, 30, 30, 130);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(255,255,255);\n"
"}")
        self.button_hide_tips = QPushButton(self.frame_settings)
        self.button_hide_tips.setObjectName(u"button_hide_tips")
        self.button_hide_tips.setGeometry(QRect(35, 10, 81, 40))
        self.button_hide_tips.setStyleSheet(u"QPushButton {	\n"
"	border: 1px solid rgb(125, 125, 125);\n"
"	border-radius: 20px;\n"
"	background-color: rgba(30, 30, 30, 70);\n"
"	border: 1px solid rgb(255,255,255);\n"
"	color: rgb(235, 235, 235);\n"
"	font: 25 10pt \"SF Pro Display\";\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(30, 30, 30, 80);\n"
"	border: 2px solid rgb(240,240,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(30, 30, 30, 130);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(255,255,255);\n"
"}")

        self.verticalLayout_3.addWidget(self.frame_settings)

        self.frame_footer = QFrame(self.page_profile)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setMinimumSize(QSize(0, 50))
        self.frame_footer.setMaximumSize(QSize(16777215, 50))
        self.frame_footer.setFrameShape(QFrame.StyledPanel)
        self.frame_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_footer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.placeholder_left = QFrame(self.frame_footer)
        self.placeholder_left.setObjectName(u"placeholder_left")
        self.placeholder_left.setFrameShape(QFrame.StyledPanel)
        self.placeholder_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.placeholder_left)

        self.madeby = QLabel(self.frame_footer)
        self.madeby.setObjectName(u"madeby")
        self.madeby.setMinimumSize(QSize(191, 0))
        self.madeby.setMaximumSize(QSize(191, 16777215))
        self.madeby.setStyleSheet(u"font: 25 16pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")
        self.madeby.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.madeby)

        self.separator = QLabel(self.frame_footer)
        self.separator.setObjectName(u"separator")
        self.separator.setMinimumSize(QSize(50, 0))
        self.separator.setMaximumSize(QSize(50, 16777215))
        self.separator.setStyleSheet(u"font: 25 16pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")
        self.separator.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.separator)

        self.bondan = QLabel(self.frame_footer)
        self.bondan.setObjectName(u"bondan")
        self.bondan.setMinimumSize(QSize(191, 0))
        self.bondan.setMaximumSize(QSize(191, 16777215))
        self.bondan.setStyleSheet(u"font: 0 16pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")
        self.bondan.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.bondan)

        self.placeholder_right = QFrame(self.frame_footer)
        self.placeholder_right.setObjectName(u"placeholder_right")
        self.placeholder_right.setFrameShape(QFrame.StyledPanel)
        self.placeholder_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.placeholder_right)


        self.verticalLayout_3.addWidget(self.frame_footer)

        self.main_page.addWidget(self.page_profile)

        self.verticalLayout.addWidget(self.main_page)


        self.horizontalLayout_3.addWidget(self.all_content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main_page.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wolf", None))
#if QT_CONFIG(tooltip)
        self.button_minimize_app.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.button_minimize_app.setText("")
#if QT_CONFIG(tooltip)
        self.button_close_app.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.button_close_app.setText("")
        self.button_home.setText("")
        self.logo.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.underline.setText(QCoreApplication.translate("MainWindow", u"________________________________________________", None))
        self.logo_2.setText(QCoreApplication.translate("MainWindow", u"olf", None))
        self.button_profile.setText("")
        self.weathercond.setText(QCoreApplication.translate("MainWindow", u"Cloudy", None))
        self.weather_icon.setText("")
        self.high_low.setText(QCoreApplication.translate("MainWindow", u"Feels like 30\u00b0. scattered clouds", None))
        self.city.setText(QCoreApplication.translate("MainWindow", u"Jakarta, ID", None))
        self.temp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">26\u00b0</span></p></body></html>", None))
        self.country.setText(QCoreApplication.translate("MainWindow", u"Monday, 21 December 2020", None))
        self.humidity.setText(QCoreApplication.translate("MainWindow", u"Humidity: 55%", None))
        self.visibility.setText(QCoreApplication.translate("MainWindow", u"Visibility: 7.0 km", None))
        self.pressure.setText(QCoreApplication.translate("MainWindow", u"Pressure: 1500 hPa", None))
        self.user_input.setText(QCoreApplication.translate("MainWindow", u"tell me a joke", None))
        self.result.setText(QCoreApplication.translate("MainWindow", u"Ir. H. Joko Widodo atau Jokowi adalah Presiden ke-7 Indonesia yang mulai menjabat sejak 20 Oktober 2014.", None))
        self.init.setText(QCoreApplication.translate("MainWindow", u"Your wish is my command.", None))
        self.commandbar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search anything you want", None))
        self.button_speak.setText("")
        self.button_command.setText("")
        self.user_name.setText(QCoreApplication.translate("MainWindow", u"Karel Bondan Andoro ", None))
        self.arrow_downleft.setText("")
        self.tip_1_up.setText(QCoreApplication.translate("MainWindow", u"Click here to change your profile pic in this app", None))
        self.profile_change.setText("")
        self.chooseyourcolor.setText(QCoreApplication.translate("MainWindow", u"Choose your color", None))
        self.separator_2.setText(QCoreApplication.translate("MainWindow", u"l", None))
        self.button_color_purplish.setText("")
        self.button_color_lime.setText("")
        self.button_color_tree.setText("")
        self.button_color_sunset.setText("")
        self.button_color_piglet.setText("")
        self.button_color_passion.setText("")
        self.button_color_nightday.setText("")
        self.button_color_biruish.setText("")
        self.button_color_timber.setText("")
        self.button_color_atlas.setText("")
        self.button_color_turqoise.setText("")
        self.button_color_lizard.setText("")
        self.button_color_sagepersuasive.setText("")
        self.button_color_predawn.setText("")
        self.button_color_darkknight.setText("")
        self.button_color_vine.setText("")
        self.button_color_hersheys.setText("")
        self.button_color_thestrain.setText("")
        self.button_color_grayscale.setText("")
        self.arrow_upright.setText("")
        self.tip_2_bottom.setText(QCoreApplication.translate("MainWindow", u"Click any of these boxes to change your theme color", None))
        self.button_edit_name.setText("")
        self.change_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your name", None))
        self.button_confirm_changename.setText("")
        self.addyourownapp.setText(QCoreApplication.translate("MainWindow", u"Miscellaneous", None))
        self.separator_3.setText(QCoreApplication.translate("MainWindow", u"l", None))
        self.button_documentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.arrow_serongkanan.setText("")
        self.tip_3_bottomright.setText(QCoreApplication.translate("MainWindow", u"Click this button to see the documentation of Wolf", None))
        self.arrow_upleft.setText("")
        self.tip_4_buttomleft.setText(QCoreApplication.translate("MainWindow", u"Click this button to change your name. Gonpachiro will call you by this name too", None))
        self.button_show_tips.setText(QCoreApplication.translate("MainWindow", u"Show tips", None))
        self.button_hide_tips.setText(QCoreApplication.translate("MainWindow", u"Hide tips", None))
        self.madeby.setText(QCoreApplication.translate("MainWindow", u"Made by", None))
        self.separator.setText(QCoreApplication.translate("MainWindow", u"l", None))
        self.bondan.setText(QCoreApplication.translate("MainWindow", u"Bondan", None))
    # retranslateUi

