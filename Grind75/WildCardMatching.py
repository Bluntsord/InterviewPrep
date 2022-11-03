from typing import *


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        left_pointer, right_pointer = 0, 0
        for i in range(len(p)):
            if left_pointer >= len(s) or right_pointer >= len(s):
                return True if p[i] == "*" else False
            elif p[i] == "?":
                right_pointer += 1
                left_pointer = right_pointer
            elif p[i] == "*":
                if i == len(p) - 1:
                    return True
                elif left_pointer >= len(s) - 1:
                    return True
                while s[right_pointer] != p[i + 1]:
                    right_pointer += 1
                left_pointer = right_pointer
            else:
                if s[left_pointer] != p[i]:
                    return False
                right_pointer += 1
                left_pointer = right_pointer

        return True if left_pointer == len(s) else False

solution = Solution()
print(solution.isMatch("v", "v*"))

