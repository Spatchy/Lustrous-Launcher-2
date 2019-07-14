from data import AppMeta
from file_manager import FileTree


def do_setup():
    path_list = list(AppMeta.DIRS.value.values())
    FileTree.create_dirs(path_list)


if AppMeta.IS_FIRST_LAUNCH:
    do_setup()
