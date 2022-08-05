from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass



    def smallest(self, nums, index):
        if index == 0:
            return nums[index + 1] > nums[index]
        return nums[index] < nums[index + 1] and nums[index] < nums[index - 1]

    def slope_up(self, nums, index):
        if index == 0:
            return nums[index + 1] > nums[index]
        return nums[index - 1] < nums[index] < nums[index + 1]

    def slope_down(self, nums, index):
        if index == 0:
            return nums[index + 1] < nums[index]
        return nums[index - 1] > nums[index] > nums[index + 1]

