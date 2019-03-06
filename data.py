import sys
import os
import file_manager
from enum import Enum


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
    IS_FROZEN = check_frozen()
    IS_FIRST_LAUNCH = check_first_launch()


class Settings:
    def __init__(self, settings_path):
        self.settings_path = settings_path

        self.search_on_start = False
        self.show_search_prompt = False
        self.solid_searchbar_background = False
        self.show_steam_button = True
        self.steam_path = "C:/Program Files(x86)/Steam/Steam.exe"
        self.do_logging = False

    def read_settings(self):
        parser = file_manager.Parse(self.settings_path)
        settings_dict = parser.parsed_json

        self.search_on_start = self.booleanize(settings_dict["search_on_start"])
        self.show_search_prompt = self.booleanize(settings_dict["show_search_prompt"])
        self.solid_searchbar_background = self.booleanize(settings_dict["solid_searchbar_background"])
        self.show_steam_button = self.booleanize(settings_dict["show_steam_button"])
        self.steam_path = settings_dict["steam_path"]
        self.do_logging = self.booleanize(settings_dict["do_logging"])

    def write_settings(self):
        settings_dict = {"search_on_start": self.search_on_start,
                         "show_search_prompt": self.show_search_prompt,
                         "solid_searchbar_background": self.solid_searchbar_background,
                         "show_steam_button": self.show_steam_button,
                         "steam_path": self.steam_path,
                         "do_logging": self.do_logging}

        file_manager.Encode(settings_dict, self.settings_path)

    @staticmethod
    def booleanize(string_to_convert):
        if string_to_convert.lower() == "true":
            return True
        else:
            return False


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
            self.theme_manifest = "./themes/" + theme_name + "/manifest.json"
            self.theme_dict = self.open_manifest()
            self.load_theme()

    def open_manifest(self):
        parser = file_manager.Parse(self.theme_manifest)
        return parser.parsed_json

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
    def __init__(self, name, banner_path, link):
        self.name = name
        self.banner_path = banner_path
        self.link = link
