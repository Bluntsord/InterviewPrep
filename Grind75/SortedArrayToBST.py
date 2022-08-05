# Definition for a binary tree node.
import math


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        middle = math.ceil(len(nums)/2)
        middle_node = TreeNode(nums[middle])
        left = self.sortedArrayToBST(nums[:middle])
        right = self.sortedArrayToBST(nums[middle:])

        middle_node.left = left
        middle_node.right = right

        return middle_node

