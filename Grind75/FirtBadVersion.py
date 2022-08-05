import math


def isBadVersion(n):
    return True

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 0, n
        while low < high:
            mid = math.floor((low + high)/2)
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low