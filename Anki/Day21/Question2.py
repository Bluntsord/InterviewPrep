from typing import *


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.memo, self.nums = {}, nums
        if sum(nums) % 2 == 1:
            return False
        self.target = sum(self.nums)/2

        return self.dp(0, 0)


    def dp(self, sum, pointer):
        key = (sum, pointer)
        if pointer >= len(self.nums) or sum > self.target:
            return False
        elif sum == self.target:
            return True
        elif key in self.memo:
            return self.memo[key]

        take_curr = self.dp(sum + self.nums[pointer], pointer + 1)
        drop_curr = self.dp(sum, pointer + 1)
        answer = take_curr or drop_curr
        self.memo[key] = answer

        return answer

nums = [1, 5, 11, 5]
solution = Solution()
print(solution.canPartition(nums))
