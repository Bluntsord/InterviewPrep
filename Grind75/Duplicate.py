class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_dict = {}
        for i in nums:
            if i in my_dict:
                return True
            my_dict[i] = i

        return False
