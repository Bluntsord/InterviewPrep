from typing import *



class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        always_same = ["0", "8", "1"]
        some_times_same = {"6":"9", "9":"6"}
        for i in range(len(num) // 2):
            left_pointer = len(num) - 1 - i
            if num[i] in always_same and num[left_pointer] == num[i]:
                continue
            elif num[i] in some_times_same and some_times_same[num[i]] == num[left_pointer]:
                continue
            return False

        if (len(num) % 2 == 1 and num[len(num) // 2] in always_same) or len(num) % 2 == 0:
            return True
        return False





solution = Solution()
s = "10"
print(solution.isStrobogrammatic(s))
