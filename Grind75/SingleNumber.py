class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_dict = {}
        for i in nums:
            if i in my_dict:
                my_dict.pop(i)
            else:
                my_dict[i] = i

        return my_dict.keys()[0]
