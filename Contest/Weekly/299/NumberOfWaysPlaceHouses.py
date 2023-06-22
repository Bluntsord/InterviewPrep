from typing import *


class Solution:
    def countHousePlacements(self, n: int) -> int:
        self.empty_plots = [1, 1, 1, 1]

        for i in range(n - 1):
            acc = sum(self.empty_plots)
            temp = self.empty_plots[2] + self.empty_plots[0]
            another_temp = self.empty_plots[1] + self.empty_plots[0]
            self.empty_plots[1] = temp
            self.empty_plots[2] = another_temp
            self.empty_plots[3] = self.empty_plots[0]
            self.empty_plots[0] = acc

        temp = (10**9) + 7
        return sum(self.empty_plots) % temp

n = 2
solution = Solution()
print(solution.countHousePlacements(n))


