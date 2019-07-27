import json
import os
import glob
# DO NOT IMPORT FROM DATA


class FileTree:

    @staticmethod
    def create_dirs(paths):
        for folder in paths:
            os.mkdir(folder)

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

    @staticmethod
    def dir_contents(path):
        return glob.glob(path)
