from typing import *
from functools import lru_cache


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        self.nums, self.k = nums, k

        return self.dp(0, k)

    @lru_cache(None)
    def dp(self, pointer, k_left):
        if pointer >= len(self.nums) and k_left == 0:
            return 0
        elif pointer >= len(self.nums) or k_left < 0:
            return float('inf')

        take_curr = max(self.nums[pointer], self.dp(pointer + 2, k_left - 1))
        drop_curr = self.dp(pointer + 1, k_left)

        answer = min(take_curr, drop_curr)

        return answer

solution = Solution()
nums = [2,3,5,9]
k = 2
print(solution.minCapability(nums, k))
