import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont, QKeySequence
from PyQt5.QtCore import *
from win32api import GetMonitorInfo, MonitorFromPoint
import re
from program_launcher import launch


class Root(QMainWindow):
    def __init__(self, theme, game_dict):
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
        self.number_of_columns = 3

        self.game_dict = game_dict

        self.sidebar = Sidebar(self)
        self.sidebar.show()
        self.grid = GameGrid(self, self.game_dict)

        self.show()

    # override eventFilter method in QObject to catch keyboard, mouse and other events:
    def eventFilter(self, obj, e):
        if e.type() == QEvent.WindowDeactivate:  # detect when window focus is lost
            print("focus lost")
            sys.exit()
        elif e.type() == QEvent.KeyPress:
            if e.key() == Qt.Key_Escape:
                print("escape pressed")
                sys.exit()
            elif re.search('[A-Z0-9]', QKeySequence(e.key()).toString()):
                print(QKeySequence(e.key()).toString())  # placeholder for search bar!

        return True

    @staticmethod
    def get_work_area_geometry():
        monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
        work_area = monitor_info.get("Work")
        return work_area[0], work_area[1], work_area[2], work_area[3]

    def get_window_geometry(self):
        return self.width, self.height


class GameGrid(QWidget):
    def __init__(self, parent, game_dict):
        # noinspection PyArgumentList
        super().__init__()

        self.parent = parent

        self.setFixedWidth(self.parent.width() - self.parent.sidebar_width)
        self.setFixedHeight(self.parent.height())

        self.game_dict = game_dict
        if self.game_dict:
            self.game_panel_list = self.create_panels()
            self.populate()
        else:
            print("game_dict is empty")
            pass  # placeholder for now

    def create_panels(self):
        game_panel_list = []
        for game_data in self.game_dict:  # each game_data is a dictionary containing data from create_game_dict()
            game_panel_list.append(GamePanel(self, game_data))
        return game_panel_list

    def populate(self):  # NUMBERS WILL CHANGE AND WILL LIKELY BE ABSTRACTED TO SETTINGS
        i = 0
        for panel in self.game_panel_list:
            panel.col = i % Root.number_of_columns
            panel.row = i / Root.number_of_columns
            x = 20 + (panel.col * 460) + (panel.col * 20)  # initial padding + width of preceding panels + padding
            y = 20 + (panel.row * 215) + (panel.row * 20)  # same as above but for height
            panel.move(x, y)
            panel.show()


class Sidebar(QWidget):
    def __init__(self, parent):
        # noinspection PyArgumentList
        super().__init__(parent)

        self.setAttribute(Qt.WA_StyledBackground)  # Allows stylesheets to work

        self.height = self.parent().height()
        self.setFixedHeight(self.height)
        self.width = self.parent().sidebar_width
        self.setFixedWidth(self.width)

        self.stylesheet_string = """background-color:black; 
        """  # currently a placeholder

        self.setStyleSheet(self.stylesheet_string)


class GamePanel(QLabel):
    def __init__(self, parent, game_data):
        super().__init__()
        self.setMouseTracking(True)

        self.parent = parent

        self.game_data = game_data
        self.banner = self.create_banner

        self.col = None  # initialize column (set by parent grid)
        self.row = None  # initialize row (set by parent grid)

        self.setPixmap(self.banner)
        self.setStyleSheet("border: 2px solid #00000000")

    def create_banner(self):
        banner_object = QPixmap(self.game_data["banner_path"])
        return banner_object

    def mouse_move_event(self, event):
        self.setStyleSheet("border: 2px solid " + Root.theme["title_outer_highlight_color"])

    def mousePressEvent(self, QMouseEvent):
        launch(self.game_data["game_path"])


def run_gui(theme, game_dict):
    app = QApplication(sys.argv)
    root = Root(theme, game_dict)
    sys.exit(app.exec_())
