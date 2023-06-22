import bisect
from typing import *

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def closestNodes(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[List[int]]
        """
        value_set = set()
        def explore_tree_dfs(node):
            if node is None:
                return

            value_set.add(node.val)
            explore_tree_dfs(node.left)
            explore_tree_dfs(node.right)

        explore_tree_dfs(root)
        nums = list(value_set)
        nums.sort()
        print(nums)
        answer = []
        for query in queries:
            smallest = bisect.bisect_right(nums, query)
            largest = bisect.bisect_left(nums, query)
            answer.append([smallest, largest])

        return answer



solution = Solution()

test = [1, 3, 4]
print(bisect.bisect_right(test, 2))




