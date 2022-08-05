# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.memo = {}

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        return max(self.helper(root), self.helper(root.left), self.helper(root.right))

    def helper(self, root):
        return self.height(root.right) + 2 + self.height(root.left)

    def height(self, root):
        if root is None:
            return 0
        elif root in self.memo:
            return self.memo[root]

        answer = 1 + max(self.height(root.left), self.height(root.right))
        self.memo[root.val] = answer
        return answer
