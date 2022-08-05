from collections import Counter
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.target = sum(nums)/2
        self.process = False
        self.acc = 0
        self.avail = []
        self.nums = nums
        self.memo = {}
        if sum(nums) % 2 == 1:
            return False
        answer = self.dp(self.target, 0)
        return answer

    def dp(self, sum, pointer):
        key = str(sum) + "|" + str(pointer)
        if sum == 0:
            return True
        elif sum < 0 or pointer >= len(self.nums):
            return False
        elif key in self.memo:
            return self.memo[key]

        result = self.dp(sum - self.nums[pointer], pointer + 1) or self.dp(sum, pointer + 1)
        self.memo[key] = result

        return result


nums = [2,2,3,3]
solution = Solution()
print(solution.canPartition(nums))




