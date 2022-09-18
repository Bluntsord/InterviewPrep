from typing import *
from collections import defaultdict
import queue as q

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stop_dict = defaultdict(set)
        for i in range(len(routes)):
            route = routes[i]
            for j in range(len(route)):
                stop = route[j]
                stop_dict[stop].add(i)

        if max(stop_dict.values(), key=len) == 1:
            return -1

        queue = q.Queue()
        visited = {}
        visited_nodes = {source: 1}
        for routes_indexes in stop_dict[source]:
            queue.put(routes_indexes)
            visited[routes_indexes] = 1

        answer = 0
        while not queue.empty():
            answer += 1
            for i in range(queue.qsize()):
                curr_route_index = queue.get()
                neighbours = routes[curr_route_index]

                for neighbour in neighbours:
                    if neighbour == target:
                        return answer
                    elif neighbour in visited_nodes:
                        continue
                    elif len(stop_dict[neighbour]) == 1:
                        continue
                    visited_nodes[neighbour] = 1

                    neighbour_indexes = stop_dict[neighbour]
                    for neighbour_index in neighbour_indexes:
                        if neighbour_index in visited:
                            continue
                        queue.put(neighbour_index)

        return -1

solution = Solution()
routes = [[1,2,7],[3,6,7]]
source = 1
target = 6
print(solution.numBusesToDestination(routes, source, target))
