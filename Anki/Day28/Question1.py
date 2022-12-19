from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_arr = [0 for _ in range(len(nums))]
        dp_arr[0] = nums[0]
        dp_arr[1] = nums[1]

        for i in range(2, len(dp_arr)):
            dp_arr[i] = max(dp_arr[i - 2] + nums[i], dp_arr[i - 1])

        print(dp_arr)

        self.memo = {}
        print(self.dp(0))

        return dp_arr[len(nums) - 1]

    def dp(self, pointer):
        if pointer >= len(nums):
            return 0
        elif pointer in self.memo:
            return self.memo[pointer]

        take = nums[pointer] + self.dp(pointer + 2)
        drop = self.dp(pointer + 1)

        answer = max(take, drop)
        self.memo[pointer] = answer

        return answer



solution = Solution()
nums = [1,2,3,1,1,2,3,2,2,1,22,2,2,1,2,3,1]
print(solution.rob(nums))

