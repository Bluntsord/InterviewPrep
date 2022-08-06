from typing import *


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = {}
        answer = 1 + self.dp(0, 0)
        return answer


    def dp(self, pointer, prev):
        key = str(pointer) + "|" + str(prev)
        if pointer >= len(self.nums):
            return 0
        elif pointer in self.memo:
            return self.memo[key]

        prev_value = self.nums[prev]
        curr = self.nums[pointer]

        if curr > prev_value:
            answer = max(1 + self.dp(pointer + 1, pointer), self.dp(pointer + 1, prev))
            self.memo[key] = answer
            return answer
        drop_current = self.dp(pointer + 1, pointer)
        self.memo[key] = drop_current
        return drop_current

nums = [10,9,2,5,3,7,101,18]
nums2 = [0, 1, 0, 3, 2, 3,4,5,67]

solution = Solution()
print(solution.lengthOfLIS(nums))
