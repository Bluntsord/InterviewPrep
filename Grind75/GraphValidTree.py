from itertools import groupby
from typing import *


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edges = list(map(lambda x: (x[0], x[1]), edges))
        if len(edges) != n - 1:
            return False
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        stack = [0]
        visited = {0: -1}

        while len(stack) != 0:

            curr_node = stack.pop()
            neighbours = self.get_neighbours(curr_node, adj_list)
            for neighbour in neighbours:
                if neighbour == visited[curr_node]:
                    continue
                if neighbour in visited:
                    return False
                visited[neighbour] = curr_node
                stack.append(neighbour)

        return len(visited) == n


    def get_neighbours(self, node, adj_list):
        return adj_list[node]


n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]

n2 = 5
edges2 = [[0,1],[0,4],[1,4],[2,3]]
solution = Solution()
print(solution.validTree(n, edges))