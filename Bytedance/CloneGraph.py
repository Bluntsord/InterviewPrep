from queue import Queue

adjList = [[2,4],[1,3],[2,4],[1,3]]

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    def cloneGraph(self, node):
        return self.dfs(node)

    def dfs(self, node):
        if node is None:
            return node

        visited = {}
        frontier = []
        frontier.append(node)

        while len(frontier) != 0:
            currNode = frontier.pop()
            if currNode.val in visited:
                newNode = visited[currNode.val]
            else:
                newNode = Node(currNode.val, [])
            visited[currNode.val] = newNode

            for neighbor in currNode.neighbors:
                newNode.neighbor.append(neighbor)
                frontier.append(neighbor)
                newNode.neighbor.sort()
        return visited[node.val]
