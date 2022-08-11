from typing import *


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_of_string = 0
        map = {}
        left_ptr = 0

        for i in range(len(s)):
            curr = s[i]
            while curr in map:
                map.pop(s[left_ptr])
                left_ptr += 1
            map[curr] = 1
            len_of_string = max(len_of_string, i - (left_ptr - 1))
        return len_of_string


s2 = "bbbbbb"
s = "pwwkew"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))