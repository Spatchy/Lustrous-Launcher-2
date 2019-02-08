import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import *


class Root(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint |
                            Qt.FramelessWindowHint |
                            Qt.WA_TranslucentBackground)

        # Set window Geometry to full screen minus task bar height
        self.width, self.height = self.get_screen_geometry()
        self.height -= 40
        self.setGeometry(0, 0, self.width, self.height)

        self.show()

    @staticmethod
    def get_screen_geometry():
        screen = QDesktopWidget().screenGeometry(-1)
        return screen.width(), screen.height()

    def get_window_geometry(self):
        return self.width, self.height


class Sidebar(QWidget):
    def __init__(self, height):
        super().__init__()

        self.height = height
        self.width = 48


class Game(QLabel):
    def __init__(self, name, banner_path, link):
        super().__init__()

        self.name = name
        self.banner_path = banner_path
        self.link = link

        self.banner = self.create_banner

        self.setPixmap(self.banner)

    def create_banner(self):
        banner_object = QPixmap(self.banner_path)
        return banner_object


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = Root()
    sys.exit(app.exec_())
