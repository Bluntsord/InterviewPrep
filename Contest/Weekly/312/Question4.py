from typing import *
from collections import defaultdict
from collections import deque


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        answer = len(vals)
        adj_list = defaultdict(set)
        val_list = defaultdict(set)
        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])
            val_list[vals[edge[0]]].add(edge[0])
            val_list[vals[edge[1]]].add(edge[1])

        possible_paths = [key for key, value in val_list.items() if len(value) > 1]
        for key in possible_paths:
            curr_queue = deque(val_list[key])
            prev_node = None
            while len(curr_queue) != 0:
                curr_node = curr_queue.popleft()
                if curr_node == key:
                    answer += 1
                neighbours = adj_list[curr_node]

                for neighbour in neighbours:
                    if prev_node and prev_node != neighbour:
                        curr_queue.appendleft(neighbour)
                prev_node = curr_node

        return answer

vals = [1,3,2,1,3]
edges = [[0,1],[0,2],[2,3],[2,4]]
solution = Solution()
print(solution.numberOfGoodPaths(vals, edges))
