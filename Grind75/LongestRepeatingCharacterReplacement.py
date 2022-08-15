from typing import *


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = dict(Counter(s))
        left_pointer = right_pointer = 0
        len_of_string = 0
        unique_letters = 0

        while right_pointer < len(s):
            right_curr = s[right_pointer]
        pass


s = "ABABBCBC"
k = 1
