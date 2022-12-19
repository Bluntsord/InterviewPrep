from typing import *
from functools import lru_cache

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        dp_dict = {}

        @lru_cache(None)
        def helper(left_pointer, right_pointer, k):
            key = (left_pointer, right_pointer, k)
            if k == len(houses):
                return 0
            elif k == 1:
                answer = self.find_median(left_pointer, right_pointer)
                dp_dict[key] = answer
                return answer
            elif k > right_pointer - left_pointer + 1 or left_pointer >= len(houses) or right_pointer >= len(houses):
                return float('inf')
            elif key in dp_dict:
                return dp_dict[key]

            answer = float('inf')
            for i in range(left_pointer, right_pointer):
                left_partition = helper(left_pointer, i, 1)
                right_partition = helper(i + 1, right_pointer, k - 1)
                answer = min(answer, left_partition + right_partition)

            dp_dict[key] = answer
            return answer

        return helper(0, len(houses) - 1, k)

    def find_median(self, left_pointer, right_pointer):
        ans = 0
        mid = (left_pointer + right_pointer) // 2
        for i in range(left_pointer, right_pointer + 1):
            ans += abs(houses[i] - houses[mid])
        return ans

solution = Solution()
houses = [1, 4, 8, 10, 20]
k = 3
print(solution.minDistance(houses, k))
# print(solution.find_median(houses, 0, 4))
