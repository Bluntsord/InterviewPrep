from typing import *
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        answer = []
        out_degree, in_degree = defaultdict(set), defaultdict(set)
        for source, destination in prerequisites:
            out_degree[source].add(destination)
            in_degree[destination].add(source)

        stack = [i for i in range(numCourses) if len(out_degree[i]) == 0]
        visited = {i: -1 for i in stack}
        while len(stack) != 0:
            curr_node = stack.pop()
            visited[curr_node] = 1
            answer.append(curr_node)
            neighbours = in_degree[curr_node]

            for neighbour in neighbours:
                if neighbour in visited:
                    continue
                neighbour_neighbours = out_degree[neighbour]
                neighbour_neighbours.remove(curr_node)
                if len(neighbour_neighbours) == 0:
                    stack.append(neighbour)

        if len(visited) != numCourses:
            return []
        return answer

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
solution = Solution()
print(solution.findOrder(numCourses, prerequisites))


