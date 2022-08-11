from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        self.root = root
        self.targetSum = targetSum
        self.answer = []
        self.curr_path = [root.val]
        self.backTracking(root, root.val)

        return self.answer

    def backTracking(self, node, curr_value):
        if node is None:
            return
        elif curr_value == self.targetSum and node.left is None and node.right is None:
            temp = self.curr_path.copy()
            self.answer.append(temp)
            return

        neighbours = self.get_neighbours(node)
        for neighbour in neighbours:
            self.curr_path.append(neighbour.val)
            next_value = curr_value + neighbour.val

            self.backTracking(neighbour, next_value)

            self.curr_path.pop()

        return


    def get_neighbours(self, node):
        answer = []
        if node.left is not None:
            answer.append(node.left)

        if node.right is not None:
            answer.append(node.right)

        return answer

solution = Solution()
first = TreeNode(1)
second = TreeNode(2)
third = TreeNode(3)
fourth = TreeNode(4)
fifth = TreeNode(5)
sixth = TreeNode(6)
seven = TreeNode(7)

first.left = second
first.right = third

second.left = fourth
second.right = sixth

third.left = seven
third.right = fifth

print(solution.pathSum(first, 9))
