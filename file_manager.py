import json


# returns the JSON content of a file when given a path to read from
class Parse:
    def __init__(self, path):
        content = self.read_file(path)
        self.parsed_json = self.parse(content)

    @staticmethod
    def read_file(path):
        with open(path, "r") as file:
            contents = file.read()
        return contents

    @staticmethod
    def parse(content):
        return json.loads(content)


# encodes json to a file when given json to encode and a path to write to
class Encode:
    def __init__(self, json_to_encode, path):
        encoded_json = self.encode(json_to_encode)
        self.write_file(encoded_json, path)

    @staticmethod
    def write_file(encoded_json, path):
        with open(path, "w") as file:
            file.write(encoded_json)

    @staticmethod
    def encode(json_to_encode):
        return json.dumps(json_to_encode)
