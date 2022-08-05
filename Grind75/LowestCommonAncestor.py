# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.descendants = {}

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.descendants = {}

    def contains(self, root, target_node):
        if root is None and target_node is None:
            return True
        elif root is None or target_node is None:
            return False




root = TreeNode(0)
first_node = TreeNode(1)
second_node = TreeNode(2)
third_node = TreeNode(3)
forth_node = TreeNode(4)

root.left = first_node
root.right = second_node
first_node.left = third_node
first_node.right = forth_node


solution = Solution()
solution.contains(root, forth_node)
temp = third_node or None
print(temp)
