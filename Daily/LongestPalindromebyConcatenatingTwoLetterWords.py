from typing import *


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_dict = dict(Counter(words))
        print(word_dict)
        answer = 0
        has_odd = 0
        for key, values in word_dict.items():
            if key[0] == key[1]:
                if values % 2 == 1:
                    has_odd = 1
                    answer -= 1
                answer += values
            else:
                key_pair = key[1] + key[0]
                answer += min(word_dict.get(key_pair, 0), values)

        return (answer + has_odd) * 2

solution = Solution()
words = ["ll","lb","bb","bx","xx","lx","xx","lx","ll","xb","bx","lb","bb","lb","bl","bb","bx","xl","lb","xx"]
print(solution.longestPalindrome(words))


