from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0

        self.target_sum = targetSum
        self.answer = 0
        self.prefix_stack = {}

        self.recursive_dfs(root, root.val)

        return self.answer

    def recursive_dfs(self, node, value):
        if node is None:
            return
        if value - self.target_sum in self.prefix_stack:
            self.answer += self.prefix_stack[value - self.target_sum]
        if value == self.target_sum:
            self.answer += self.prefix_stack[value]

        self.prefix_stack[value] = self.prefix_stack.get(value, 0) + 1
        neighbours = self.get_neighbours(node)
        for neighbour in neighbours:
            next_value = value + neighbour.val

            self.recursive_dfs(neighbour, next_value)

        if self.prefix_stack[value] == 1:
            self.prefix_stack.pop(value)
        else:
            self.prefix_stack[value] -= 1


    def get_neighbours(self, node):
        answer = []
        if node.left is not None:
            answer.append(node.left)
        if node.right is not None:
            answer.append(node.right)
        return answer

tenth_node = TreeNode(10)
fifth_node = TreeNode(5)
third_node = TreeNode(3)
third_node2 = TreeNode(3)
minus2_node = TreeNode(-2)
two_node = TreeNode(2)
one_node = TreeNode(1)
minus3_node = TreeNode(-3)
eleven_node = TreeNode(11)

tenth_node.left = fifth_node
tenth_node.right = minus3_node
minus3_node.right = eleven_node
fifth_node.left = third_node
fifth_node.right = two_node
third_node.left = third_node2
third_node.right = minus2_node
two_node.right = one_node

root = tenth_node
solution = Solution()
print(solution.pathSum(root, 8))
