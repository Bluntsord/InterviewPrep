from typing import *


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s_arr = [(i, s_char) for i, s_char in enumerate(s)]
        vowel_arr = list(filter(lambda x: x[1] in vowels, s_arr))
        new_vowel_arr = []
        for i in range(len(vowel_arr)):
            curr = (vowel_arr[i][0], vowel_arr[-i -1][1])
            s_arr[vowel_arr[i][0]] = curr

        temp = list(map(lambda x: x[1], s_arr))
        answer = "".join(temp)

        return answer

solution = Solution()
s = "aA"
print(solution.reverseVowels(s))
