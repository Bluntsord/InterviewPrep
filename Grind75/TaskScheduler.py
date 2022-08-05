import queue
from typing import *
from queue import PriorityQueue

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        my_dict = Counter(tasks)
        list_dict = list(my_dict.values())
        max_count = max(my_dict.items())
        all_maxes = list(filter(lambda x: x == max_count[1], list_dict))

        answer = (all_maxes[0] - 1) * (n + 1) + len(all_maxes)
        return answer


tasks = ["A","A","A","B","B","B"]
solution = Solution()
print(solution.leastInterval(tasks, 0))





