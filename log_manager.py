import datetime
import file_manager
from data import AppMeta


class DumpLog:
    def __init__(self, raw_string):
        self.string_to_dump = raw_string
        self.manipulate_string()
        self.do_dump()

    def manipulate_string(self):
        current_time = datetime.datetime.now()
        self.string_to_dump = str(current_time) + " | " + self.string_to_dump

    def do_dump(self):
        file_manager.Dump(self.string_to_dump, AppMeta.LOG_PATH, file_manager.DumpMode.Append)

