import bisect
from typing import *
from functools import lru_cache

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        self.index_dict = {}

        @lru_cache(None)
        def dp(stick_start, stick_end):
            start_index = self.get_index(stick_start)
            end_index = self.get_index(stick_end)
            if end_index - start_index == 0 or stick_start == stick_end:
                return 0

            addition = float('inf')
            for partition in cuts:
                if partition <= stick_start or partition >= stick_end:
                    continue

                left_partition = dp(stick_start, partition)
                right_partition = dp(partition, stick_end)
                addition = min(addition, left_partition + right_partition + stick_end - stick_start)

            return 0 if addition == float('inf') else addition

        return dp(0, n)

    def get_index(self, stick_pos):
        if stick_pos not in self.index_dict:
            start_index = bisect.bisect_left(cuts, stick_pos)
            self.index_dict[stick_pos] = start_index
        else:
            start_index = self.index_dict[stick_pos]

        return start_index

solution = Solution()
n = 10
cuts = [7,8,9,2,1]
print(solution.minCost(n, cuts))
