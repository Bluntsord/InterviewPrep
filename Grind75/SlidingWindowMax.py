from typing import *
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        self.k = k
        self.dq = deque()
        for i in range(k):
            self.handle_deq((nums[i], i))
        print(self.dq)

        helper = [self.dq[0]]
        for i in range(k, len(nums)):
            print(self.dq)
            self.handle_deq((nums[i], i))
            helper.append(self.dq[0])

        answer = list(map(lambda x: x[0], helper))
        return answer


    def handle_deq(self, num):
        while self.dq and num[1] - self.dq[0][1] >= self.k:
            self.dq.popleft()

        while self.dq and self.dq[-1] <= num:
            self.dq.pop()
        self.dq.append(num)




nums = [1,3,1,2,0,5]
k = 3
solution = Solution()
print(solution.maxSlidingWindow(nums, k))