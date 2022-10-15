from typing import *
from collections import defaultdict
import queue as q

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        self.adj_list = defaultdict(set)
        for i in range(len(routes)):
            curr_route = routes[i]
            for j in range(len(curr_route)):
                self.adj_list[curr_route[j]].add(i)

        if len(self.adj_list[source]) == 0:
            return -1

        queue = q.Queue()
        answer, visited = 0, {}
        for route_index in self.adj_list[source]:
            queue.put(route_index)
            visited[route_index] = -1

        while not queue.empty():
            for i in range(queue.qsize()):
                curr_route = queue.get()
                neighbours = routes[curr_route]

                for neighbour in neighbours:
                    if neighbour == target:
                        return answer + 1

                    for neighbour_routes in self.adj_list[neighbour]:
                        if neighbour_routes in visited:
                            continue
                        visited[neighbour_routes] = curr_route
                        queue.put(neighbour_routes)


            answer += 1
        return -1

# routes = [[1,2,7],[3,6,7]]
# source, target = 1, 6

routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
source, target = 15, 12
solution = Solution()
print(solution.numBusesToDestination(routes, source, target))

