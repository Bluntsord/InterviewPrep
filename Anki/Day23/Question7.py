from typing import *

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp_grid = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in reversed(range(n)):
            for j in reversed(range(n)):
                curr_iteration = n - 1 + i - j
                take_left = nums[i] * multipliers[curr_iteration] + dp_grid[i - 1][j] if i > 0 else 0
                take_right = nums[j] * multipliers[curr_iteration] + dp_grid[i][j - 1] if j > 0 else 0
                dp_grid[i][j] = max(take_left, take_right)

        return dp_grid[0][0]




nums = [-5,-3,-3,-2,7,1]
multipliers = [-10,-5,3,4,6]
# nums = [1,2,3]
# multipliers = [3,2,1]
solution = Solution()
print(solution.maximumScore(nums, multipliers))
