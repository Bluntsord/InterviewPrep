from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.number = 0
        self.k = k
        self.answer = None
        self.isProcessed = False
        self.backTracking()
        return self.answer

    def backTracking(self, root):
        if self.isProcessed:
            return
        elif self.number == self.k:
            self.answer = root
            self.isProcessed = True

        self.backTracking(root.left)
        self.number += 1
        self.backTracking(root.right)


