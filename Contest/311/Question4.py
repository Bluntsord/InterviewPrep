from typing import *



class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.word_dict = dict(Counter(words))
        self.memo = {}
        print(self.word_dict)

    def dp(self, word):
        if len(word) == 0:
            return 0
        elif len(word) == 1:
            return self.word_dict[word]
        elif word in self.memo:
            return self.memo[word]

        current_prefix = word[0]
        answer = self.dp(current_prefix)
        for i in range(1, len(word)):
            current_prefix += word[i]
            answer += self.dp(current_prefix)

words = ["a", "ab", "abc", "cab"]
solution = Solution()
print(solution.sumPrefixScores(words))
