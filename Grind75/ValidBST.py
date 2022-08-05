# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(float('-inf'), float('inf'), root)

    def helper(self, lower_limit, upper_limit, root):
        if root is None:
            return True
        elif root.val <= lower_limit or root.val >= upper_limit:
            return False

        check_left = self.helper(lower_limit, root.val, root.left)
        check_right = self.helper(root.val, upper_limit, root.right)

        return check_left and check_right


