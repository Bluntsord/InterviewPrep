from typing import *


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        base = left_pointer = right_pointer = -1
        answer = 0
        for i in range(len(nums)):
            if not minK <= nums[i] <= maxK:
                base = i

            if nums[i] == minK:
                left_pointer = i
            elif nums[i] == maxK:
                right_pointer = i

            answer += max(0, min(right_pointer, left_pointer) - base)

        return answer


nums = [1, 1, 1, 1]
minK = 1
maxK = 1

solution = Solution()
print(solution.countSubarrays(nums, minK, maxK))



