from typing import *
from functools import lru_cache

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left_pointer = answer = 0
        curr_window = {}

        for r in range(len(s)):
            curr_window[s[r]] = 1 + curr_window.get(s[r], 0)

            while r - left_pointer + 1 - max(curr_window.items(), key=lambda x: x[1])[1] > k:
                curr_window[s[left_pointer]] -= 1
                left_pointer += 1

            answer = max(answer, r - left_pointer + 1)
        return answer

solution = Solution()
s = "ABAA"
k = 0
print(solution.characterReplacement(s, k))

