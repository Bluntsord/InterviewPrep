from typing import *


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Getting the max of each and comparing would get the highest already
        horizontalCuts.sort()
        verticalCuts.sort()
        max_horizontal = 0
        verticalCuts.insert(0, 0)
        verticalCuts.append(w)

        for i in range(1, len(verticalCuts)):
            temp = verticalCuts[i] - verticalCuts[i - 1]
            max_horizontal = max(max_horizontal, temp)

        max_vertical = 0
        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)

        for i in range(1, len(horizontalCuts)):
            temp = horizontalCuts[i] - horizontalCuts[i - 1]
            max_vertical = max(max_vertical, temp)

        return (max_vertical * max_horizontal) % (10**9 + 7)


h = 5
w = 4
horizontalCuts = [3, 1]
verticalCuts = [1]
solution = Solution()
print(solution.maxArea(h, w, horizontalCuts, verticalCuts))