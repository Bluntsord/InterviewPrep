from typing import List

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodeMap = {}
        for child, parent in prerequisites:
            if parent not in nodeMap:
                nodeMap[parent] = Node(parent, [])

            if child not in nodeMap:
                nodeMap[child] = Node(child, [])

            nodeMap[parent].neighbors.append(nodeMap[child])

        self.visited = [False] * numCourses
        self.curr_path = [False] * numCourses

        for nodes in nodeMap.values():
            if self.hasCycle(nodes):
                return False
        return True

        # Essentially cycle detection in a graph
        # Use dfs for cycle detection

    def hasCycle(self, root):
        if self.visited[root.val]:
            return False
        elif self.curr_path[root.val]:
            return True

        self.curr_path[root.val] = True

        for neighbour in root.neighbors:
            if self.hasCycle(neighbour):
                return True

        self.curr_path[root.val] = False
        self.visited[root.val] = True

        return False

numCourses = 3
prerequisites = [[1,0]]
prerequisites2 = [[1,0], [1,2]]
solution = Solution()
print(solution.canFinish(numCourses, prerequisites2))