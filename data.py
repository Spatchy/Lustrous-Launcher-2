import sys
import file_manager


# Contains/generates various metadata
class AppMeta:
    def __init__(self):
        self.VERSION = "2.0.0"
        self.REPOSITORY = "https://spatchy.github.io/Lustrous-Launcher-2"
        self.RELEASE = "/releases/latest"
        self.SETTINGS_PATH = "./settings.json"
        self.LOG_PATH = "./ll.log"
        self.IS_FROZEN = self.check_frozen()

    @staticmethod
    def check_frozen():
        if hasattr(sys, "frozen"):
            return True
        else:
            return False


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
                         "do_logging":self.do_logging}

        file_manager.Encode(settings_dict, self.settings_path)

    @staticmethod
    def booleanize(string_to_convert):
        if string_to_convert.lower() == "true":
            return True
        else:
            return False


class ThemeEngine:
    def __init__(self, theme_name):

        # set default values
        self.primary_color = "#D83434"  # the primary accent color
        self.background_color = "#000000"  # the background color of the launcher
        self.background_alpha = 70  # the transparency of the background of the launcher
        self.sidebar_background_color = "#060606"  # the background color of the sidebar
        self.button_outer_highlight_color = "#222222"  # the outer highlight when a button is hovered over
        self.title_outer_highlight_color = "#777777"  # the outer highlight when a game is hovered over
        self.title_inner_highlight_color = self.primary_color  # the color of a game selected for editing
        self.searchbar_background_color = self.sidebar_background_color  # the color of the searchbar

        if theme_name is not None:
            self.theme_manifest = "./themes/" + theme_name + "/manifest.json"
            self.theme_dict = self.open_manifest()
            self.load_theme()

    def open_manifest(self):
        parser = file_manager.Parse(self.theme_manifest)
        return parser.parsed_json

    def load_theme(self):
        self.primary_color = self.theme_dict["primary_color"]
        self.background_color = self.theme_dict["background_color"]
        self.background_alpha = int(self.theme_dict["background_alpha"])
        self.sidebar_background_color = self.theme_dict["sidebar_background_color"]
        self.button_outer_highlight_color = self.theme_dict["button_outer_highlight_color"]
        self.title_outer_highlight_color = self.theme_dict["title_outer_highlight_color"]
        self.title_inner_highlight_color = self.theme_dict["title_inner_highlight_color"]
        self.searchbar_background_color = self.theme_dict["searchbar_background_color"]
