from typing import *


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0

        possible_windows = []
        for i in range(len(weights) - 1):
            possible_windows.append(weights[i] + weights[i + 1])

        possible_windows.sort()
        return sum(possible_windows[-(k - 1):]) + sum(possible_windows[:k - 1])

solution = Solution()
weights = [1,3,5,1]
k = 2