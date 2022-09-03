from typing import *

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {}
        if len(edges) > n:
            return False
        for edge in edges:
            first_node, second_node = edge[0], edge[1]
            adj_list[first_node] = adj_list.get(first_node, []) + [second_node]
            adj_list[second_node] = adj_list.get(second_node, []) + [first_node]

        stack = [0]
        visited = {0: 1}
        while len(stack) != 0:
            curr_node = stack.pop()

            neighbours = adj_list[curr_node]

            for neighbour in neighbours:
                if neighbour not in visited:
                    visited[neighbour] = 1
                    stack.append(neighbour)

        print(visited)
        return len(visited) == n

n = 5
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
solution = Solution()
print(solution.validTree(n, edges))