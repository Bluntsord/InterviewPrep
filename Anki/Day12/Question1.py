from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.answer = []
        self.target_sum = targetSum
        self.acc = []

        self.backTracking(root, root.val)

        return self.answer


    def backTracking(self, node, curr_sum):
        if curr_sum == self.target_sum:
            temp = self.acc.copy()
            self.answer.append(temp)

        if node is None:
            return None

        neighbours = self.get_neighbours(node)
        for neighbour in neighbours:
            next_sum = curr_sum + neighbour.val
            self.acc.append(node.val)

            self.backTracking(neighbour, next_sum)

            self.acc.pop()


    def get_neighbours(self, node):
        if node is None:
            return []
        answer = []
        if node.left is not None:
            answer.append(node.left)
        if node.right is not None:
            answer.append(node.right)

        return answer

node_dict = {i: TreeNode(i) for i in range(14)}

node_dict[5].left = node_dict[4]
node_dict[4].left = node_dict[11]
node_dict[11].left = node_dict[7]
node_dict[11].right = node_dict[2]
node_dict[5].right = node_dict[8]
node_dict[8].left = node_dict[13]
node_dict[8].right = node_dict[4]
node_dict[6].left = node_dict[5]
node_dict[6].right = node_dict[1]

head = node_dict[5]
solution = Solution()
print(solution.pathSum(head, 24))


