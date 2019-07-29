from data import AppMeta
from data import Game
from data import DefaultSettings
from data import DefaultTheme
from file_manager import FileTree
from exceptions import *
from collections import OrderedDict


def do_setup():
    path_list = list(AppMeta.DIRS.value.values())
    FileTree.create_dirs(path_list)


def create_game_dict():  # creates alphabetized OrderedDict of all games from games dir
    game_dict = OrderedDict()
    for file in FileTree.dir_contents(AppMeta.DIRS["games"]):
        file_json = FileTree.read_file(file)
        game_title = file_json["title"]
        game_path = file_json["path"]
        banner_name = file_json["banner_path"]
        platform = file_json["platform"]
        game_dict[game_title] = Game(game_title, game_path, banner_name, platform)
    return game_dict


class SettingsEngine:
    settings_dict = None

    @classmethod
    def bind_settings_dict(cls):  # binds settings_dict to the settings file only once created
        cls.settings_dict = FileTree.read_file(AppMeta.SETTINGS_PATH.value)

    @classmethod
    def apply_default_settings(cls):
        cls.settings_dict = OrderedDict()  # probably best to keep this ordered
        # noinspection PyTypeChecker
        for member in DefaultSettings:  # convert default settings to ordered dict
            cls.settings_dict[str(member.name).lower()] = member.value
        FileTree.write_file(cls.settings_dict, AppMeta.SETTINGS_PATH.value)  # json.dumps handles OrderedDicts fine
        cls.bind_settings_dict()

    @classmethod
    def change_setting(cls, setting_to_change, new_value):
        cls.settings_dict[setting_to_change] = new_value

    @classmethod
    def write_settings(cls):
        FileTree.write_file(cls.settings_dict, AppMeta.settings_path)


class ThemeEngine:
    PROTOCOL_VERSION = "1.0.0"
    theme_dict = None

    @classmethod
    def load_theme(cls, theme_name=None):
        if theme_name is None:
            cls.load_default_theme()
        else:
            theme_manifest = AppMeta.DIRS["themes"] + theme_name + "/manifest.json"
            cls.theme_dict = cls.open_manifest(theme_manifest)
            if cls.theme_dict["protocol_version"] > cls.PROTOCOL_VERSION:
                raise InvalidThemeException(InvalidThemeException.string)

    @classmethod
    def open_manifest(cls, theme_manifest):
        return FileTree.read_file(theme_manifest)

    @classmethod
    def load_default_theme(cls):
        cls.theme_dict = OrderedDict()  # probably best to keep this ordered
        # noinspection PyTypeChecker
        for member in DefaultTheme:  # convert default settings to ordered dict
            cls.theme_dict[str(member.name).lower()] = member.value


# Is immediately run on program launch
if __name__ == "__main__":
    if AppMeta.IS_FIRST_LAUNCH:
        # do_setup()
        # SettingsEngine.apply_default_settings()
        pass
    else:
        # SettingsEngine.bind_settings_dict()
        pass
