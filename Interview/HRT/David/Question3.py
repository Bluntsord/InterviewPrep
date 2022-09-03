from typing import *


class Solution:
    def __init__(self):
        self.history = []

    def operation(self, command, text):
        if command == "INSERT":
            curr = (text, self.insert_command)
            function = self.insert_command
            self.history.append(curr)
            return  function
        elif command == "BACKSPACE":
            curr = (text, self.backspace_command)
            function = self.backspace_command
            self.history.append(curr)
            return function
        else:
            curr = (text, self.undo_command)
            self.history.append(curr)
            return self.undo_command

    def insert_command(self, text, word_to_add):
        return text + word_to_add

    def backspace_command(self, text, number):
        return text[:len(text) - number]

    def undo_command(self):
        return self.history[-1][0]

