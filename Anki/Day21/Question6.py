from typing import *
import queue as q


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = q.Queue()
        queue.put(root)
        answer = []

        while not queue.empty():
            curr_level = []
            for i in range(queue.qsize()):
                curr_node = queue.get()
                neighbours = self.get_neighbour(curr_node)
                curr_level.append(curr_node.val)

                for neighbour in neighbours:
                    queue.put(neighbour)
            answer.append(curr_level)
        return answer


    def get_neighbour(self, curr_node):
        if curr_node is None or (curr_node.left is None and curr_node.right is None):
            return []
        elif curr_node.left is None:
            return [curr_node.right]
        elif curr_node.right is None:
            return [curr_node.left]
        return [curr_node.left, curr_node.right]
