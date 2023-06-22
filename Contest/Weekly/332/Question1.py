from typing import *


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums) // 2):
            answer += int(str(nums[i]) + str(nums[len(nums) - i - 1]))

        print(answer)
        if len(nums) % 2 == 1:
            answer += nums[len(nums) // 2]

        return answer

solution = Solution()
nums = [5,14,13,8,12]
print(solution.findTheArrayConcVal(nums))