import bisect
import functools
from typing import *
import sys

class Solution(object):
    def maxValue(self, events, k):
        memo = {}
        events.sort(key=lambda x: (x[0], x[1]))

        @functools.lru_cache(None)
        def dp(pointer, events_left):
            if pointer >= len(events) or events_left <= 0:
                return 0

            start = bisect.bisect_right(events, events[pointer][1], key=lambda x: x[0])
            take_curr = events[pointer][2] + dp(start, events_left - 1)
            drop_curr = dp(pointer + 1, events_left)
            answer = max(take_curr, drop_curr)

            return answer

        answer = dp(0, k)
        return answer

solution = Solution()
events = [[1,2,4],[3,4,3],[2,3,10]]
k = 2
print(solution.maxValue(events, k))