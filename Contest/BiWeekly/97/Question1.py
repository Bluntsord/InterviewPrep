from typing import *


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            for letter in str(num):
                answer.append(int(letter))

        return answer

solution = Solution()
nums = [13,25,83,77]
print(solution.separateDigits(nums))
