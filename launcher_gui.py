import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import *
from win32api import GetMonitorInfo, MonitorFromPoint


class Root(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint |
                            Qt.FramelessWindowHint |
                            Qt.WA_TranslucentBackground)

        # Set window Geometry to full screen minus task bar height. NEW: now accounts for any task bar height/location
        monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
        work_area = monitor_info.get("Work")
        self.setGeometry(work_area[0], work_area[1], work_area[2], work_area[3])

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = Root()
    sys.exit(app.exec_())
