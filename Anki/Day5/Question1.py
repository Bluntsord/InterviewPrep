from typing import *


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.wordDict = wordDict
        self.word_dict = {key: 1 for key in wordDict}
        self.len_word_dict = {}
        self.memo = {}
        for key in self.word_dict.keys():
            if len(key) not in self.len_word_dict:
                self.len_word_dict[len(key)] = 1

        answer = self.dp(0)
        return answer

    def dp(self, pointer):
        if pointer > len(self.s):
            return False
        elif pointer == len(self.s):
            return True
        elif pointer in self.memo:
            return self.memo[pointer]

        answer = False
        for lengths in self.len_word_dict.keys():
            curr_substring = self.s[pointer: pointer + lengths + 1]
            if curr_substring in self.word_dict:
                answer = answer or self.dp(pointer + lengths + 1)
            else:
                continue

        self.memo[pointer] = answer
        return answer






