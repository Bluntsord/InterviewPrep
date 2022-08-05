import math


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_dict = {}
        ln = math.floor(len(nums)/2)
        for i in nums:
            if i in nums and my_dict[i] + 1 > ln:
                return i
            elif i in nums:
                my_dict[i] += 1
            else:
                my_dict[i] = 1

        return -1