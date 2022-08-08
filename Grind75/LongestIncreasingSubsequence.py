import time
from typing import *
import sys


class Solution:
    def main(self, nums):
        start_time = time.time()
        self.lengthOfLIS(nums)
        end_time = time.time()
        return start_time - end_time

    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = {}
        answer = self.dp(0, float('-inf'))
        return answer


    def dp(self, pointer, prev):
        key = str(pointer) + "|" + str(prev)
        if pointer >= len(self.nums):
            return 0
        elif key in self.memo:
            return self.memo[key]

        curr = self.nums[pointer]

        if curr > prev:
            take_curr = 1 + self.dp(pointer + 1, curr)
        else:
            take_curr = -1
        drop_current = self.dp(pointer + 1, prev)
        answer = max(drop_current, take_curr)
        self.memo[key] = answer
        return answer


x = 1
solution = Solution()
for i in range(10):
    x *= 2
    temp = list(range(x))
    print(solution.main(temp))

