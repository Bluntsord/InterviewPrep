class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.memo = {}

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
       """
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if left_height > right_height + 1 or left_height < right_height - 1:
            return False

        answer = True and self.isBalanced(root.left) and self.isBalanced(root.right)
        return answer



    def height(self, root):
        if root is None:
            return 0
        elif root in self.memo:
            return self.memo[root]
        answer = 1 + max(self.height(root.right), self.height(root.left))
        return answer


