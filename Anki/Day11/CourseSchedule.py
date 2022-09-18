from typing import *


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.outdegree = {i: [] for i in range(numCourses)}
        self.indegree = {i: [] for i in range(numCourses)}
        for edge in prerequisites:
            start, end = edge[0], edge[1]
            self.outdegree[start] = self.outdegree.get(start, []) + [end]
            self.indegree[end] = self.indegree.get(end, []) + [start]
        stack = [key for key, value in self.outdegree.items() if len(value) == 0]
        visited = {}

        while len(stack) != 0:
            curr_node = stack.pop()
            visited[curr_node] = 1
            neighbours = self.indegree[curr_node]
            for neighbour in neighbours:
                if neighbour in visited:
                    continue

                neighbour_neighbours = self.outdegree[neighbour]
                neighbour_neighbours.remove(curr_node)
                if len(neighbour_neighbours) == 0:
                    stack.append(neighbour)
                self.outdegree[neighbour] = neighbour_neighbours

        return len(visited) == numCourses

numCourses = 2
prerequisites = [[1,0],[0,1]]
solution = Solution()
print(solution.canFinish(numCourses, prerequisites))





