from typing import *
import queue as q

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.answer = []
        self.root = root

        queue = q.Queue()
        queue.put(root)
        visited = {}

        while not queue.empty():
            curr = []
            for i in range(queue.qsize()):
                curr_node = queue.get()
                curr.append(curr_node.val)

                neighbours = self.get_neighbours(curr_node)
                for neighbour in neighbours:
                    if neighbour not in visited:
                        visited[neighbour.val] = 1
                        queue.put(neighbour)
            self.answer.append(curr)
        self.answer.reverse()
        return self.answer


    def get_neighbours(self, node):
        if node is None:
            return None
        answer = []
        if node.left is not None:
            answer.append(node.left)
        if node.right is not None:
            answer.append(node.right)
        return answer