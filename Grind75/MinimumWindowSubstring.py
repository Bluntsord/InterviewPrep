from typing import *


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        map = dict(Counter(t))
        left_ptr = right_ptr = 0
        head = 0
        len_of_string = len(s)
        unique_letters = len(map)

        while right_ptr < len(s):
            right_curr = s[right_ptr]
            if right_curr in map:
                map[right_curr] -= 1
                if map[right_curr] == 0:
                    unique_letters -= 1
            right_ptr += 1

            while unique_letters == 0:
                left_curr = s[left_ptr]
                if left_curr in map:
                    map[left_curr] += 1
                    if map[left_curr] > 0:
                        unique_letters += 1
                if right_ptr - left_ptr < len_of_string:
                    len_of_string = right_ptr - left_ptr
                    head = left_ptr
                left_ptr += 1

        return "" if len_of_string == len(s) else s[head: head + len_of_string]

solution = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(solution.minWindow(s, t))


