class Solution(object):
    def __init__(self):
        self.memo = {}
        self.nums = None
        self.mult = None

    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        self.memo = {}
        self.nums = nums
        self.mult = multipliers
        return self.dp(0, 0)

    def dp(self, first_ptr, second_ptr):
        key = str(first_ptr) + "|" + str(second_ptr)
        if second_ptr >= len(self.mult):
            return 0
        elif key in self.memo:
            return self.memo[key]

        take_first = self.mult[second_ptr]


