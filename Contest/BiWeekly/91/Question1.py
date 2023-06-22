from typing import *


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        answer = set()

        while len(nums) != 0:
            curr_min, curr_max = nums.pop(0), nums.pop()
            answer.add((curr_min + curr_max)/ 2)

        return len(answer)

nums = [1, 100]
solution = Solution()
print(solution.distinctAverages(nums))
