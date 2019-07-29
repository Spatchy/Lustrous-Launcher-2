import sys
import os
from file_manager import FileTree
from aenum import Enum, NoAlias
from collections import OrderedDict


# Contains/generates various metadata
class AppMeta(Enum):

    @staticmethod
    def check_frozen():
        if hasattr(sys, "frozen"):
            return True
        else:
            return False

    @staticmethod
    def check_first_launch():
        if os.path.isdir("./games"):
            return False
        else:
            return True

    VERSION = "2.0.0"
    REPOSITORY = "https://spatchy.github.io/Lustrous-Launcher-2"
    RELEASE = "/releases/latest"
    SETTINGS_PATH = "./settings.json"
    LOG_PATH = "./ll.log"
    DIRS = OrderedDict([("games", "./games"),  # order must be maintained so subdirectories are created properly
                        ("shortcuts", "./games/shortcuts"),
                        ("steam shortcuts", "./games/shortcuts/steam"),
                        ("banners", "./banners"),
                        ("banner packs", "./banners/bannerpacks"),
                        ("themes", "./themes")])
    IS_FROZEN = check_frozen.__func__()  # PyCharm marks this a potentially bad, it's not
    IS_FIRST_LAUNCH = check_first_launch.__func__()  # PyCharm marks this a potentially bad, it's not


class DefaultSettings(Enum):
    _settings_ = NoAlias  # allow multiple members to have the same value

    SEARCH_ON_START = False
    SHOW_SEARCH_PROMPT = False
    SOLID_SEARCHBAR_BACKGROUND = False
    SHOW_STEAM_BUTTON = True
    STEAM_PATH = "C:/Program Files(x86)/Steam/Steam.exe"
    DO_LOGGING = False


class DefaultTheme(Enum):
    __settings__ = NoAlias  # allow multiple members to have the same value

    PRIMARY_COLOR = "#D83434"  # the primary accent color
    BACKGROUND_COLOR = "#000000"  # the background color of the launcher
    BACKGROUND_ALPHA = 70  # the transparency of the background of the launcher
    SIDEBAR_BACKGROUND_COLOR = "#060606"  # the background color of the sidebar
    BUTTON_OUTER_HIGHLIGHT_COLOR = "#222222"  # the outer highlight when a button is hovered over
    TITLE_OUTER_HIGHLIGHT_COLOR = "#777777"  # the outer highlight when a game is hovered over
    TITLE_INNER_HIGHLIGHT_COLOR = PRIMARY_COLOR  # the color of a game selected for editing
    SEARCHBAR_BACKGROUND_COLOR = SIDEBAR_BACKGROUND_COLOR  # the color of the searchbar


class Game:
    def __init__(self, name, banner_path, link, platform):
        self.name = name
        self.banner_path = banner_path
        self.link = link
        self.platform = platform
