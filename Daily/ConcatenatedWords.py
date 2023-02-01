from typing import *

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.lengths_set = set()
        for word in words:
            self.lengths_set.add(len(word))
        self.words_set = set(words)

        answer = filter(lambda x: self.word_break(x), words)
        return list(answer)

    def word_break(self, curr_word):
        self.word = curr_word
        self.memo = {}
        answer = self.dp(0)
        return answer

    def dp(self, pointer):
        if pointer > len(self.word):
            return False
        elif pointer == len(self.word):
            return True
        elif pointer in self.memo:
            return self.memo[pointer]

        answer = False
        for length in self.lengths_set:
            curr_answer = False
            if length >= len(self.word):
                continue

            curr_word = self.word[pointer: pointer + length]
            if curr_word in self.words_set:
                curr_answer = self.dp(pointer + length)

            answer = answer or curr_answer

        self.memo[pointer] = answer
        return answer

solution = Solution()
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(solution.findAllConcatenatedWordsInADict(words))