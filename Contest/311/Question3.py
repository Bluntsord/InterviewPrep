from typing import *
import queue as q

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = q.Queue()
        queue.put(root)
        is_odd = False

        while not queue.empty():
            for node in reversed(queue):
                pass

