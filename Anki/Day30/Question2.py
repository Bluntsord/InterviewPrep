from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = dict(Counter(nums))
        for key, values in num_dict.items():
            if values >= len(nums) // 2:
                return key

        return  -1

