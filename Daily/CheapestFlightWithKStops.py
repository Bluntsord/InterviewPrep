from typing import *
from collections import defaultdict
from queue import PriorityQueue

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for source, destination, price in flights:
            adj_list[source].append((destination, price))
        priority_queue = PriorityQueue()
        priority_queue.put((0, 0, src))
        visited = {src: 0}
        answer = float('inf')

        while not priority_queue.empty():
            distance_from_src, number_of_stops, curr_stop = priority_queue.get()
            neighbours = adj_list[curr_stop]
            visited[curr_stop] = number_of_stops

            if curr_stop == dst:
                return answer

            for neighbour, next_distance in neighbours:
                if neighbour in visited and visited[neighbour] <= number_of_stops:
                    continue
                elif number_of_stops > k:
                    continue
                priority_queue.put((distance_from_src + next_distance, number_of_stops + 1, neighbour))

        return -1 if answer == float('inf') else answer

solution = Solution()
n = 11
flights = [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
src = 0
dst = 2
k = 4
print(solution.findCheapestPrice(n, flights, src, dst, k))




