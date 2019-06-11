import json
from enum import Enum
import os


class FileTree:  # IN PROGRESS OF MOVING EVERYTHING INTO HERE

    @staticmethod
    def do_setup():
        os.mkdir("./games")
        os.mkdir("./games/steamgames")
        os.mkdir("./games/steamgames/shortcuts")
        os.mkdir("./banners")
        os.mkdir("./banners/bannerpacks")
        os.mkdir("./themes")

    @staticmethod
    def dump(raw_string, path, mode="w"):
        with open(path, mode) as file:
            file.write(raw_string)

    @staticmethod
    def write_file(json_to_encode, path):
        encoded_json = json.dumps(json_to_encode)
        with open(path, "w") as file:
            file.write(encoded_json)

    @staticmethod
    def read_file(path):
        with open(path, "r") as file:
            contents = file.read()
        return json.loads(contents)
