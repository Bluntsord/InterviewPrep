from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        self.mapping = {}
        for word in words:
            key = len(word)
            if key not in self.mapping:
                self.mapping[key] = set()
            self.mapping[key].add(word)
        self.memo = {}
        min_length = min(self.mapping.keys())
        self.mapping[0] = ""
        answer = 0
        for pos in self.mapping[min_length]:
            answer = max(answer, self.dp(pos))
        return answer - min_length + 1 if answer > 0 else 1

    def dp(self, last_string):
        if len(last_string) + 1 not in self.mapping:
            return len(last_string)
        elif last_string in self.memo:
            return self.memo[last_string]

        neighbours = self.mapping[len(last_string) + 1]
        answer = 0
        for neighbour in neighbours:
            if self.is_predecessor(last_string, neighbour):
                answer = max(answer, self.dp(neighbour))

        self.memo[last_string] = answer
        return answer

    def is_predecessor(self, parent_word, child_word):
        if len(child_word) - len(parent_word) != 1:
            return False

        for i in range(len(child_word)):
            temp = child_word[:i] + child_word[i + 1:]
            if temp == parent_word:
                return True

        return False

first_word = "abc"
second_word = "acb"
third_word = "abcd"
forth_word = "cabd"
words = ["a","b","ab", "bac"]
words2 = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
solution = Solution()
print(solution.longestStrChain(words))




