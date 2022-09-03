from typing import *
import queue as q

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = q.Queue()
        queue.put((root, 0))
        visited = {root.val: 1}
        max_width = -1

        while not queue.empty():
            curr_level_max = 0
            for i in range(queue.qsize()):
                temp = queue.get()
                curr_node, curr_node_val = temp[0], temp[1]

                handle_left = 0
                handle_right = 0

                if curr_node.left is not None and curr_node.left not in visited:
                    handle_left = (curr_node.left, curr_node_val * 2)
                    queue.put(handle_left)

                if curr_node.right is not None and curr_node.right not in visited:
                    handle_right = (curr_node.right, curr_node_val * 2 + 1)
                    queue.put(handle_right)
                curr_level_max = max(handle_left, handle_right)

            max_width = max(max_width, curr_level_max)

        return max_width


tree_nodes = [TreeNode(i) for i in range(10)]
tree_nodes[1].left = tree_nodes[3]
tree_nodes[3].left = tree_nodes[5]
tree_nodes[3].left = tree_nodes