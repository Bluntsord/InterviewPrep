from typing import *

class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        if node1 == node2:
            return node1

        self.edges = edges
        first_arr = self.bfs(node1, [-1 for i in range(len(edges))], 0, set())
        second_arr = self.bfs(node2, [-1 for i in range(len(edges))], 0, set())


        curr_min, answer = float('inf'), -1
        for i in range(len(first_arr)):
            if first_arr[i] == -1 or second_arr[i] == -1:
                continue

            curr = max(first_arr[i], second_arr[i])
            if curr < curr_min:
                curr_min = curr
                answer = i

        return answer

    def bfs(self, node, arr, level, visited):
        if node in visited:
            return arr

        arr[node] = level
        visited.add(node)

        if self.edges[node] == -1:
            return arr

        neighbour = self.edges[node]
        level += 1
        return self.bfs(neighbour, arr, level, set())


solution = Solution()
edges = [1, 2, -1]
node1 = 0
node2 = 2
print(solution.closestMeetingNode(edges, node1, node2))



