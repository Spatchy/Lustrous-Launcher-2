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


class Theme(Enum):
    # set default values
    primary_color = "#D83434"  # the primary accent color
    background_color = "#000000"  # the background color of the launcher
    background_alpha = 70  # the transparency of the background of the launcher
    sidebar_background_color = "#060606"  # the background color of the sidebar
    button_outer_highlight_color = "#222222"  # the outer highlight when a button is hovered over
    title_outer_highlight_color = "#777777"  # the outer highlight when a game is hovered over
    title_inner_highlight_color = primary_color  # the color of a game selected for editing
    searchbar_background_color = sidebar_background_color  # the color of the searchbar


class ThemeEngine:
    def __init__(self, theme_name):
        if theme_name is not None:
            self.theme_manifest = AppMeta.DIRS["themes"] + theme_name + "/manifest.json"
            self.theme_dict = self.open_manifest()
            self.load_theme()

    def open_manifest(self):
        return FileTree.read_file(self.theme_manifest)

    @staticmethod
    def load_theme():
        Theme.primary_color = Theme.theme_dict["primary_color"]
        Theme.background_color = Theme.theme_dict["background_color"]
        Theme.background_alpha = int(Theme.theme_dict["background_alpha"])
        Theme.sidebar_background_color = Theme.theme_dict["sidebar_background_color"]
        Theme.button_outer_highlight_color = Theme.theme_dict["button_outer_highlight_color"]
        Theme.title_outer_highlight_color = Theme.theme_dict["title_outer_highlight_color"]
        Theme.title_inner_highlight_color = Theme.theme_dict["title_inner_highlight_color"]
        Theme.searchbar_background_color = Theme.theme_dict["searchbar_background_color"]


class Game:
    def __init__(self, name, banner_path, link, platform):
        self.name = name
        self.banner_path = banner_path
        self.link = link
        self.platform = platform
