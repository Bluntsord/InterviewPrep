import queue
from typing import *

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        priority_queue = queue.PriorityQueue()
        initial = (temperatures[0], 0)
        priority_queue.put(initial)
        answer = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while priority_queue.qsize() != 0 and priority_queue.queue[0][0] < temperatures[i]:
                curr = priority_queue.get()
                answer[curr[1]] = i - curr[1]
            temp = (temperatures[i], i)
            priority_queue.put(temp)

        return answer

temperatures = [73,74,75,71,69,72,76,73]
solution = Solution()
print(solution.dailyTemperatures(temperatures))




