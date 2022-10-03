from typing import *
from queue import PriorityQueue

def minimizeCost(arr):
    answer = 0
    pq = PriorityQueue()
    for num in arr:
        pq.put(num)
    while pq.qsize() > 1:
        first, second = pq.get(), pq.get()
        answer += first + second
        pq.put(first + second)
    return answer

# arr = [30, 10, 20, 25]
# arr = [30, 25, 20, 10]
arr = [95, 37, 33, 19, 92, 94, 16, 2, 18, 50]
expected = 1358
print(minimizeCost(arr))

