class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_ptr = 0

        for non_zero_ptr in range(len(nums)):
            if nums[non_zero_ptr] != 0:
                nums[zero_ptr], nums[non_zero_ptr] = nums[non_zero_ptr], nums[zero_ptr]
                zero_ptr += 1
        return nums


solution = Solution()
nums2 = [0,1,0,3,12]
nums = [1, 0]
print(solution.moveZeroes(nums))