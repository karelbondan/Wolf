from main import *

# the function to drag the window around when pressed on the title bar, and to make the
# minimize and close button works.
class UIFunctions(MainWindow):
    def remove_title(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        self.ui.all_content.setGraphicsEffect(self.shadow)

        # minimize the window when the minimize button is pressed
        self.ui.button_minimize_app.clicked.connect(lambda: self.showMinimized())

        # closes the app when the close button is pressed
        self.ui.button_close_app.clicked.connect(lambda: self.close())