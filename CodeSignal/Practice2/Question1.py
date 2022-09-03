from typing import *


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.word_dict = {word for word in wordDict}
        self.length_dict = sorted(list({len(key) for key in self.word_dict}), reverse=True)
        self.memo = {}

        answer = self.dp(0)
        return answer

    def dp(self, pointer):
        if pointer > len(self.s):
            return False
        elif pointer == len(self.s):
            print(pointer)
            return True
        elif pointer in self.memo:
            return self.memo[pointer]

        answer = False
        print(self.length_dict)
        for word_lengths in self.length_dict:
            if s[pointer: pointer + word_lengths] in self.word_dict:
                wish = self.dp(pointer + word_lengths)
            else:
                wish = False
            answer = answer or wish

        self.memo[pointer] = answer
        return answer





s = "leetcode"
wordDict = ["leet","code"]
solution = Solution()
print(solution.wordBreak(s, wordDict))

s1 = "catsandog"
wordDict1 = ["cats","dog","sand","and","cat"]
print(solution.wordBreak(s1, wordDict1))