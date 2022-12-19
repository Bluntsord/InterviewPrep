from typing import *
from functools import lru_cache

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def dp(pointer, fuel_left):
            if pointer < 0 or pointer >= len(locations):
                return 0
            elif fuel_left == 0:
                return 1 if pointer == finish else 0

            answer = 0 if pointer != finish else 1
            for i in range(len(locations)):
                cost = abs(locations[pointer] - locations[i])
                if i == pointer or fuel_left - cost < 0:
                    continue
                answer += dp(i, fuel_left - cost)

            return answer % mod

        return dp(start, fuel)

solution = Solution()
locations = [4, 3, 1]
start = 1
finish = 0
fuel = 6
print(solution.countRoutes(locations, start, finish, fuel))

