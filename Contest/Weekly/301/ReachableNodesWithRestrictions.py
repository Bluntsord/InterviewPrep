from itertools import groupby
from typing import *


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        stack = [0]
        visited = {0: 1}
        adj_list = {}
        edges = list(map(lambda x: (x[0], x[1]), edges))
        for i in range(len(edges)):
            curr = edges[i]
            if curr[0] not in adj_list:
                adj_list[curr[0]] = [curr[1]]
            else:
                adj_list[curr[0]].append(curr[1])

        if curr[1] not in adj_list:
            adj_list[curr[1]] = [curr[0]]
        else:
            adj_list[curr[1]].append(curr[0])

        answer = 0
        restricted_dict = {}
        for i in restricted:
            restricted_dict[i] = 1
        while len(stack) != 0:
            curr_node = stack.pop()
            answer += 1
            neighbours = adj_list[curr_node]

            for neighbour in neighbours:
                if neighbour not in visited and neighbour not in restricted_dict:
                    visited[neighbour] = 1
                    stack.append(neighbour)

        return answer