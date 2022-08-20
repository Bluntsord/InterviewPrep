from typing import *


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_dict = {}
        left_pointer = right_pointer = 0
        answer = 0

        while right_pointer < len(s):
            right_letter = s[right_pointer]
            while right_letter not in char_dict and len(char_dict) == 2:
                left_letter = s[left_pointer]
                if char_dict[left_letter] == 1:
                    char_dict.pop(left_letter)
                else:
                    char_dict[left_letter] -= 1
                left_pointer += 1
            char_dict[right_letter] = char_dict.get(right_letter, 0) + 1
            answer = max(answer, right_pointer - left_pointer + 1)
            right_pointer += 1

        return answer

s = "eceba"
s = "ccaabbb"
solution = Solution()
print(solution.lengthOfLongestSubstringTwoDistinct(s))


