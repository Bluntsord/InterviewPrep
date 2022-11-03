from typing import *


class Solution:
    def oddString(self, words: List[str]) -> str:
        difference_array_dict = {}
        another_dict = {}
        for word in words:
            curr_difference_array = self.get_difference_array(word)
            another_dict[curr_difference_array] = word
            difference_array_dict[curr_difference_array] = difference_array_dict.get(curr_difference_array, 0) + 1

        print(another_dict)
        print(difference_array_dict)
        answer = []
        for key, value in difference_array_dict.items():
            if value == 1:
                answer = another_dict[key]

        return answer

    def get_difference_array(self, word):
        answer = []
        for i in range(1, len(word)):
            answer.append(ord(word[i]) - ord(word[i - 1]))

        return tuple(answer)

solution = Solution()
words = ["ddd","poo","baa","onn"]
print(solution.oddString(words))