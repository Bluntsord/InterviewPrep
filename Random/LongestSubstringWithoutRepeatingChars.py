from typing import *


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left_pointer = right_pointer = 0
        answer = -1
        while right_pointer < len(s):
            right_letter = s[right_pointer]
            while right_letter in char_set:
                left_letter = s[left_pointer]
                char_set.remove(left_letter)
                left_pointer += 1
            answer = max(answer, right_pointer - left_pointer + 1)
            char_set.add(right_letter)
            right_pointer += 1

        return answer

s = "abcabcbb"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))