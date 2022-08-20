from typing import *
import queue as q

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        is_opposite_direction = False
        queue = q.Queue()
        queue.put(root)
        visited = {root: -1}
        answer = []

        while not queue.empty():
            curr_level = []
            for i in range(queue.qsize()):
                curr_node = queue.get()
                curr_level.append(curr_node)
                neighbours = self.get_neighbour(curr_node)

                for neighbour in neighbours:
                    if neighbour not in visited:
                        visited[neighbour] = 1
                        queue.put(neighbour)
            if is_opposite_direction:
                curr_level = reversed(curr_level)
            is_opposite_direction = not is_opposite_direction
            answer.extend(curr_level)
        return answer







    def get_neighbour(self, node):
        answer = []
        if node.right is not None:
            answer.append(node.right)
        if node.left is not None:
            answer.append(node.left)
        return answer