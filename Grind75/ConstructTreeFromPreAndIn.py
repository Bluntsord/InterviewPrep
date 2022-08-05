from queue import Queue
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.answer = []
        root = self.recurse(preorder, inorder)
        return root

    def recurse(self, preorder, inorder):
        if len(preorder) == 0 and len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        wish_left = self.recurse(preorder[1: mid + 1], inorder[:mid])
        wish_right = self.recurse(preorder[mid + 1:], inorder[mid + 1:])
        root.left = wish_left
        root.right = wish_right
        return root


preorder = [1, 2]
inorder = [2, 1]

solution = Solution()
print(solution.buildTree(preorder, inorder))
