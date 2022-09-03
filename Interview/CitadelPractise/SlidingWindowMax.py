from typing import *
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        for i in range(k):
            if len(deq) != 0 and deq[0] > nums[i]:
                deq.append(nums[i])
            elif len(deq) != 0 and deq[0] < nums[i]:
                deq.clear()
                deq.append(nums[i])

        for i in range(k, len(nums)):
            deq.popleft()
        pass