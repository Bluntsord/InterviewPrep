from collections import defaultdict
from typing import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        out_degree, in_degree = defaultdict(set), defaultdict(set)
        for source, destination in prerequisites:
            out_degree[source].add(destination)
            in_degree[destination].add(source)

        for i in range(numCourses):
            out_degree[i] = out_degree.get(i, set())
            in_degree[i] = in_degree.get(i, set())

        no_neighbours_stack = [key for key, value in out_degree.items() if len(value) == 0]
        visited = set([node for node in no_neighbours_stack])

        while len(no_neighbours_stack) != 0:
            curr_node = no_neighbours_stack.pop()
            neighbours = in_degree[curr_node]
            visited.add(curr_node)

            for neighbour in neighbours:
                if neighbour in visited:
                    continue
                neighbour_neighbours = out_degree[neighbour]
                neighbour_neighbours.remove(curr_node)
                if len(neighbour_neighbours) == 0:
                    no_neighbours_stack.append(neighbour)

        if len(visited) == numCourses:
            return True
        return False


