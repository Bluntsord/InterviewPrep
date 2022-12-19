from typing import *


class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        dp_array = [0 for _ in range(numPeople + 1)]
        dp_array[0] = dp_array[1] = 1
        mod_factor = 10 ** 9 + 7

        for i in range(2, (len(dp_array) // 2) + 1):
            for j in range(1, i + 1):
                dp_array[i] = (dp_array[i] + dp_array[i - j] * dp_array[j - 1]) % mod_factor

        for i in reversed(range(len(dp_array))):
            if dp_array[i] != 0:
                return dp_array[i]

        return 1

solution = Solution()
print(solution.numberOfWays(6))
