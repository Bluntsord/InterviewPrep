from typing import *

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []

        def dfs(node):
            if node is None:
                return

            answer.append(node.val)
            wish_left = dfs(node.left)
            wish_right = dfs(node.right)

        dfs(root)
        return answer
