import json


# returns the JSON content of a file when given a path to read from
class Parser:
    def parse_file(self, path):
        content = self.read_file(path)
        parsed_json = self.parse(content)
        return parsed_json

    @staticmethod
    def read_file(path):
        with open(path, "r") as file:
            contents = file.read()
        return contents

    @staticmethod
    def parse(content):
        return json.loads(content)


# encodes json to a file when given json to encode and a path to write to
class Encoder:
    def encode_json(self, json_to_encode, path):
        encoded_json = self.encode(json_to_encode)
        self.write_file(encoded_json, path)
        return True

    @staticmethod
    def write_file(encoded_json, path):
        with open(path, "w") as file:
            file.write(encoded_json)

    @staticmethod
    def encode(json_to_encode):
        return json.dumps(json_to_encode)


# create parser and encoder objects
parser = Parser
encoder = Encoder
