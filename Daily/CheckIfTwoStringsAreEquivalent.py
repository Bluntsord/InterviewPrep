from typing import *


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first_word, second_word = ''.join(word1), ''.join(word2)
        return first_word == second_word