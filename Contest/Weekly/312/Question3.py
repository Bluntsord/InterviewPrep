import bisect
from typing import *


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        non_increasing, non_decreasing = self.get_non_increasing_ranges(nums), self.get_non_decreasing_ranges(nums)
        answer = []
        for i in range(k, len(nums) - k):
            left_side = (i - k, i - 1)
            right_side = (i + 1, i + k)
            temp = self.check_in_range(non_increasing, left_side)
            another = self.check_in_range(non_decreasing, right_side)
            if temp and another:
                answer.append(i)

        return answer

    def check_in_range(self, stack, side):
        # print(stack)
        # print(side)
        insert_order = bisect.bisect_left(stack, side[0], key=lambda x: x[0])
        # print(insert_order)
        if (insert_order == 0 and stack[0][0] > side[0]) \
                or stack[insert_order - 1][1] < side[1]:
            # print("False")
            return False
        # print("True")
        # print("=====")
        return True

    def get_non_decreasing_ranges(self, nums):
        non_decreasing = []
        left_pointer, right_pointer = 1, 1
        while right_pointer < len(nums):
            right_num = nums[right_pointer]
            while right_num >= nums[right_pointer - 1]:
                right_pointer += 1
                if right_pointer >= len(nums):
                    break
                right_num = nums[right_pointer]
            non_decreasing.append((left_pointer - 1, right_pointer - 1))
            left_pointer = right_pointer + 1
            right_pointer = left_pointer
        return non_decreasing

    def get_non_increasing_ranges(self, nums):
        non_decreasing = []
        left_pointer, right_pointer = 1, 1
        while right_pointer < len(nums):
            right_num = nums[right_pointer]
            while right_num <= nums[right_pointer - 1]:
                right_pointer += 1
                if right_pointer >= len(nums):
                    break
                right_num = nums[right_pointer]
            non_decreasing.append((left_pointer - 1, right_pointer - 1))
            left_pointer = right_pointer + 1
            right_pointer = left_pointer
        return non_decreasing


nums = [2,1,1,1,3,4,1]
# nums = [2,1,1,2]
k = 2
solution = Solution()
print(solution.goodIndices(nums, k))

