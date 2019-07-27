from data import AppMeta
from data import Game
from file_manager import FileTree
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


# Is immediately run on program launch
if __name__ == "__main__":
    if AppMeta.IS_FIRST_LAUNCH:
        do_setup()
