from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        self.nums = nums
        return self.dp(0, True)

    def dp(self, pointer, canRob):
        key = str(pointer) + str(canRob)
        if not canRob:
            return self.dp(pointer + 1, True)
        elif pointer >= len(self.nums):
            return 0
        elif key in self.memo:
            return self.memo[key]

        rob_current = self.nums[pointer] + self.dp(pointer + 1, False)
        ignore_current = self.dp(pointer + 1, True)
        answer = max(rob_current, ignore_current)
        self.memo[key] = answer

        return answer

nums = [1,2,3,1]
nums2 = [2,7,9,3,1]
solution = Solution()
print(solution.rob(nums2))


