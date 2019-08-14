import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import *
from win32api import GetMonitorInfo, MonitorFromPoint


class Root(QWidget):
    def __init__(self, theme):
        # noinspection PyArgumentList
        super().__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint |
                            Qt.FramelessWindowHint |
                            Qt.WA_TranslucentBackground)

        # Set window Geometry to full screen minus task bar height
        self.setGeometry(*self.get_work_area_geometry())

        self.installEventFilter(self)

        # set GUI-wide variables
        self.theme = theme
        self.sidebar_width = 48
        self.grid_padding = 20

        self.sidebar = Sidebar(self)
        self.sidebar.show()

        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            sys.exit()

    def eventFilter(self, obj, e):
        if e.type() == QEvent.WindowDeactivate:
            print("focus lost")
            sys.exit()
        return True

    @staticmethod
    def get_work_area_geometry():
        monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
        work_area = monitor_info.get("Work")
        return work_area[0], work_area[1], work_area[2], work_area[3]

    def get_window_geometry(self):
        return self.width, self.height


class GameGrid(QWidget):
    def __init__(self):
        # noinspection PyArgumentList
        super().__init__()

        self.setFixedWidth(self.parent().width-Root.sidebar_width)
        self.setFixedHeight(self.parent().height)


class Sidebar(QWidget):
    def __init__(self, parent):
        # noinspection PyArgumentList
        super().__init__(parent)

        self.setAttribute(Qt.WA_StyledBackground)  # Allows stylesheets to work

        self.height = self.parent().height()
        self.setFixedHeight(self.height)
        self.width = self.parent().sidebar_width
        self.setFixedWidth(self.width)

        self.setStyleSheet("background-color:black;")  # Placeholder only

    # def paintEvent(self, QPaintEvent):
    #     QStyleOption().__init__(self)
    #     painter = QStylePainter(self)
    #     painter.style()



class GamePanel(QLabel):
    def __init__(self, game_object):
        super().__init__()
        self.setMouseTracking(True)

        self.game = game_object
        self.banner = self.create_banner

        self.setPixmap(self.banner)
        self.setStyleSheet("border: 2px solid #00000000")

    def create_banner(self):
        banner_object = QPixmap(self.banner_path)
        return banner_object

    def mouse_move_event(self, event):
        self.setStyleSheet("border: 2px solid " + Root.theme["title_outer_highlight_color"])


def run_gui(theme):
    app = QApplication(sys.argv)
    root = Root(theme)
    sys.exit(app.exec_())
