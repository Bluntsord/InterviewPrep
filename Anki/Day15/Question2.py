from typing import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_acc, left_arr = 1, []
        for num in nums:
            left_acc *= num
            left_arr.append(left_acc)
        right_acc, right_arr = 1, []
        for num in reversed(nums):
            right_acc *= num
            right_arr.append(right_acc)
        right_arr = list(reversed(right_arr))

        answer = []
        for i in range(len(nums)):
            if i == 0:
                answer.append(right_arr[1])
            elif i == len(nums) - 1:
                answer.append(left_arr[len(nums) - 2])
            else:
                temp = left_arr[i - 1] * right_arr[i + 1]
                answer.append(temp)
        return answer

solution = Solution()
nums = [1,2,3,4]
print(solution.productExceptSelf(nums))