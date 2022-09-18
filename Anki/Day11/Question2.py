from typing import *
import queue as q

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = {i: set() for i in range(n)}
        for edge in edges:
            adj_list.get(edge[0], set()).add(edge[1])
            adj_list.get(edge[1], set()).add(edge[0])
        queue = q.Queue()
        for key, value in adj_list.items():
            if len(value) == 1:
                queue.put(key)
        visited = n

        while queue.qsize() != 0:
            for i in range(queue.qsize()):
                curr_node = queue.get()
                neighbours = adj_list[curr_node]
                visited -= 1
                for neighbour in neighbours:
                    neighbour_neighbours = adj_list[neighbour]
                    neighbour_neighbours.remove(curr_node)
                    if len(neighbour_neighbours) == 1:
                        queue.put(neighbour)
            if visited <= 2:
                return list(queue.queue)
        return list(queue.queue)

n = 4
edges = [[1,0],[1,2],[1,3]]

n2 = 6
edges2 = [[3,0],[3,1],[3,2],[3,4],[5,4]]
solution = Solution()
print(solution.findMinHeightTrees(n2, edges2))
