from typing import *
from collections import Counter

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        visited = []
        for word in queries:
            for dict_word in dictionary:
                if self.distance_between_words(word, dict_word) <= 2:
                    visited.append(word)
                    break

        return list(visited)

    def distance_between_words(self, first_word, second_word):
        answer = 0
        for i in range(len(first_word)):
            if first_word[i] != second_word[i]:
                answer += 1

        return answer

solution = Solution()
print(solution.distance_between_words("note", "joke"))
print('====')
queries1 = ["word","note","ants","wood"]
dictionary1 = ["wood","joke","moat"]
print(solution.twoEditWords(queries1, dictionary1))