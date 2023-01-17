from typing import *
import queue as q

class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        adj_list = {i: [] for i in range(n)}
        for source, destination in edges:
            adj_list[source].append(destination)
            adj_list[destination].append(source)

        queue = q.Queue()
        propagate = {i: {labels[i]: 1} for i in range(n)}
        for node, neighbours in adj_list.items():
            if len(neighbours) == 1:
                queue.put(node)

        visited = set()

        while not queue.empty():
            for i in range(queue.qsize()):
                curr_node = queue.get()
                neighbours = adj_list[curr_node]

                for neighbour in neighbours:
                    if neighbour in visited:
                        continue

                    visited.add(neighbour)
                    propagate[neighbour][labels[neighbour]] += 1
                    queue.put(neighbour)

        answer = [propagate[i][labels[i]] for i in range(n)]
        print(propagate)

        return answer

solution = Solution()
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
labels = "abaedcd"
print(solution.countSubTrees(n, edges, labels))




