class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        elif root.val == subRoot.val:
            return self.isSameTree(root, subRoot)

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSameTree(self, root, other_root):
        if root is None and other_root is None:
            return True
        elif root is None or other_root is None:
            return False

        temp = self.isSameTree(root.left, other_root.left)
        return root.val == other_root.val and temp and self.isSameTree(root.right, other_root.right)

