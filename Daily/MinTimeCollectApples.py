from typing import *

class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """

        # This only works because the graph is a tree. Hence there is only one path of getting to each node
        answer = 0
        adj_list = {source: [] for source in range(n)}
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        visited = set()

        def backTracking(node):
            nonlocal answer
            if node is None:
                return False

            neighbours = self.get_neighbours(node, adj_list)
            curr_tree_has_apple = hasApple[node]
            for neighbour in neighbours:
                if (node, neighbour) in visited or (neighbour, node) in visited:
                    continue

                visited.add((node, neighbour))
                curr = backTracking(neighbour)
                curr_tree_has_apple = curr or curr_tree_has_apple

            if curr_tree_has_apple:
                answer += 2

            return curr_tree_has_apple

        backTracking(0)
        return max(answer - 2, 0)


    def get_neighbours(self, node, adj_list):
        return adj_list[node]

solution = Solution()
n = 4
edges = [[0,2],[0,3],[1,2]]
hasApple = [False, True, False, False]
print(solution.minTime(n, edges, hasApple))
