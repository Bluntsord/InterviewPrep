from typing import *


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left_pointer = answer = 0

        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[left_pointer])
                left_pointer += 1
            answer = max(answer, i - left_pointer + 1)
            char_set.add(s[i])

        return answer

solution = Solution()
s = "au"
print(solution.lengthOfLongestSubstring(s))



