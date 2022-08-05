from typing import *

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = {}
        max_so_far = nums[0]
        min_so_far = nums[0]
        answer = max_so_far

        for numbers in nums[1:]:
            temp_max = max(numbers, min_so_far * numbers, max_so_far * numbers)
            min_so_far = min(numbers, min_so_far * numbers, max_so_far * numbers)

            max_so_far = temp_max
            answer = max(max_so_far, answer)

        return answer

nums = [-3, -3, -1]
# nums = [3, 2, -1, 4]

solution = Solution()
print(solution.maxProduct(nums))
