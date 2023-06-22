from typing import *
import queue as q
from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        self.adj_list = defaultdict(set)
        for source, destination in edges:
            self.adj_list[source].add(destination)
            self.adj_list[destination].add(source)

        bob_path = self.get_bob_path()
        bob_path_set = {bob_path[i]: i for i in range(len(bob_path))}
        pq = q.Queue()
        cum_sum = amount[0]
        answer = amount[0]
        pq.put((amount[0], 0, 0))
        visited = {0: -1}

        while not pq.empty():
            curr_cost, curr_node, curr_level = pq.get()
            if curr_level == 0:
                continue
            elif curr_node in bob_path_set and bob_path_set[curr_node] <= curr_level:
                cum_sum += 0
            elif curr_level < len(bob_path) and curr_node == bob_path[curr_level]:
                cum_sum += curr_cost/2
            else:
                cum_sum += curr_cost
            answer = min(answer, cum_sum)

            neighbours = self.adj_list[curr_node]
            for neighbour in neighbours:
                if neighbour in visited:
                    continue
                visited[neighbour] = curr_node
                pq.put((amount[neighbour], neighbour, curr_level + 1))

        return cum_sum



    def get_bob_path(self):
        queue = q.Queue()
        queue.put(0)
        visited = {0: -1}

        while not queue.empty():
            curr_node = queue.get()
            if curr_node == bob:
                break
            neighbours = self.adj_list[curr_node]

            for neighbour in neighbours:
                if neighbour in visited:
                    continue
                visited[neighbour] = curr_node
                queue.put(neighbour)

        bob_curr = bob
        bob_path = [bob_curr]
        while bob_curr != 0:
            bob_curr = visited[bob_curr]
            bob_path.append(bob_curr)

        return bob_path



solution = Solution()
edges = [[0,1],[0,2]]
bob = 2
amount = [-3360,-5394,-1146]
# edges = [[0,1],[1,2],[1,3],[3,4]]
# bob = 3
# amount = [-2,4,2,-4,6]
print(solution.mostProfitablePath(edges, bob, amount))



