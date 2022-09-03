from typing import *


class Fancy:
    ADD_ALL = "addAll"
    APPEND = "append"
    MULT_ALL = "multAll"
    GET_INDEX = "getIndex"

    def __init__(self):
        self.arr = []
        self.off_set_sequence = []
        self.append_history = {}
        self.command = 0

    def handle_command(self, command_string, query_arr):
        if command_string == self.APPEND:
            self.append(query_arr[0])
        elif command_string == self.ADD_ALL:
            self.ADD_ALL(query_arr[0])
        elif command_string == self.MULT_ALL:
            self.multAll(query_arr[0])
        elif command_string == self.GET_INDEX:
            self.getIndex(query_arr[0])
        self.command += 1
        return

    def plus(self, start, value):
        return start + value

    def mult(self, start, value):
        return start * value

    def do_nothing(self, start):
        return start

    def append(self, val: int) -> None:
        # Handle offset
        self.off_set_sequence.append(self.do_nothing)

        # Trying to get the index that was joined
        self.append_history[self.off_set_sequence] = 0


    def addAll(self, inc: int) -> None:
        pass

    def multAll(self, m: int) -> None:
        pass

    def getIndex(self, idx: int) -> int:
        pass
