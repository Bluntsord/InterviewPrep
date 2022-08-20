from typing import *


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.adj_list = self.generate_adj_list(edges)
        self.visited = {}
        self.counter = 0
        for nodes in self.adj_list.keys():
            self.counter += self.dfs(nodes)

        if len(self.adj_list.keys()) != n:
            self.counter += (len(self.adj_list.keys()) - n)
        return self.counter

    def dfs(self, node):
        if node in self.visited:
            return 0

        stack = [node]
        self.visited[node] = 1

        while len(stack) != 0:
            curr_node = stack.pop()
            neighbours = self.get_neighbours(curr_node)

            for neighbour in neighbours:
                if neighbour not in self.visited:
                    self.visited[neighbour] = 1
                    stack.append(neighbour)

        return 1

    def get_neighbours(self, node):
        return self.adj_list[node]

    def generate_adj_list(self, edges):
        adj_list = {}
        for edge in edges:
            if edge[0] in adj_list:
                curr = adj_list[edge[0]]
                curr.append(edge[1])
            else:
                adj_list[edge[0]] = [edge[1]]

            if edge[1] in adj_list:
                curr = adj_list[edge[1]]
                curr.append(edge[0])
            else:
                adj_list[edge[1]] = [edge[0]]
        return adj_list




n = 5
edges = [[0,1],[1,2],[3,4]]

n2 = 5
edges2 = [[0,1],[1,2],[2,3],[3,4]]
solution = Solution()

print(solution.countComponents(n, edges))
print(solution.countComponents(n2, edges2))
