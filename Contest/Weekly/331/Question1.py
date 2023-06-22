from typing import *
from queue import PriorityQueue

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = PriorityQueue()
        for i in gifts:
            pq.put(-i)

        for i in range(k):
            curr = int((- 1 * pq.get()) ** 0.5)
            pq.put(-curr)

        answer = 0
        while not pq.empty():
            answer -= pq.get()

        return answer

gifts = [25,64,9,4,100]
k = 4
solution = Solution()
print(solution.pickGifts(gifts, k))

