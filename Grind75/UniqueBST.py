from typing import *


class Solution:
    def numTrees(self, n: int) -> int:
        dp_array = [0 for _ in range(n + 1)]
        dp_array[0], dp_array[1], dp_array[2] = 1, 1, 2

        for i in range(3, n + 1):
            for j in range(i):
                left = j
                right = i - j - 1
                dp_array[i] += dp_array[left] * dp_array[right]

        return dp_array[n]

solution = Solution()
print(solution.numTrees(4))