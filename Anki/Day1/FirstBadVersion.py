from typing import *


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n

        while low < high:
            mid = math.floor((low + high) / 2)
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low

n = 5
bad = 4

solution = Solution()
print(solution.firstBadVersion(n))


