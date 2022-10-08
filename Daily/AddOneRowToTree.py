# Definition for a binary tree node.
from typing import *
import queue as q

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        queue = q.Queue()
        queue.put(root)

        while not queue.empty():
            level = 1
            for i in range(queue.qsize()):
                curr_node = queue.get()
                neighbours = self.get_neighbours(curr_node)

                for neighbour in neighbours:
                    queue.put(neighbour)

    def get_neighbours(self, curr_node):
        if curr_node is None or (curr_node.left is None and curr_node.right is None):
            return []
        elif curr_node.right is None:
            return [curr_node.left]
        return [curr_node.right]



