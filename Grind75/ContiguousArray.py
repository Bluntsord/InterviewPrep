from typing import *


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums_dict = {}
        counter = 0
        answer = 0
        for i in range(len(nums)):
            curr = nums[i]
            if counter in nums_dict:
                answer = max(answer, i - nums_dict[counter])
            else:
                nums_dict[counter] = i
            if curr == 1:
                counter += 1
            else:
                counter -= 1

        if counter in nums_dict:
            answer = max(answer, len(nums) - nums_dict[counter])

        return answer

nums = [1, 0, 1, 1, 0, 0]


solution = Solution()
print(solution.findMaxLength(nums))