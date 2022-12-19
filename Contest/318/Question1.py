from typing import *


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        answer = [nums[i] for i in range(len(nums)) if nums[i] != 0]
        answer += [0] * (len(nums) - len(answer))

        return answer

nums = [1,2,2,1,1,0]
solution = Solution()
print(solution.applyOperations(nums))
