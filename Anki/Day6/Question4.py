from typing import *


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.word_dict = {word: 1 for word in wordDict}
        self.len_dict = {}
        self.memo = {}
        for word in wordDict:
            self.len_dict[len(word)] = 1

        return self.dp(0)


    def dp(self, pointer):
        if pointer > len(self.s):
            return False
        elif pointer == len(self.s):
            return True
        elif pointer in self.memo:
            return self.memo[pointer]

        answer = False
        for lengths in self.len_dict.keys():
            curr_string = self.s[pointer: pointer + lengths]
            if curr_string in self.word_dict:
                answer = answer or self.dp(pointer + lengths)

        self.memo[pointer] = answer
        return answer

s = "leetcode"
wordDict = ["leet","code"]
solution = Solution()
print(solution.wordBreak(s, wordDict))