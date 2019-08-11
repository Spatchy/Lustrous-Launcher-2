import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import *
from processor import ThemeEngine
from win32api import GetMonitorInfo, MonitorFromPoint


class Root(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint |
                            Qt.FramelessWindowHint |
                            Qt.WA_TranslucentBackground)

        # Set window Geometry to full screen minus task bar height
        self.setGeometry(*self.get_work_area_geometry())

        self.installEventFilter(self)

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


class Sidebar(QWidget):
    def __init__(self, height):
        super().__init__()

        self.height = height
        self.width = 48


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
        self.setStyleSheet("border: 2px solid " + ThemeEngine.theme_dict["title_outer_highlight_color"])


def run_gui():
    app = QApplication(sys.argv)
    root = Root()
    sys.exit(app.exec_())
