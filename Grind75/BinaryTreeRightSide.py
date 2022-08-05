from queue import Queue
from typing import Optional
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = []
        self.bfs(root)
        return self.answer

    def bfs(self, root):
        queue = Queue()
        queue.put(root)

        visited = {root.val: 1}

        while not queue.empty():
            q_size = queue.qsize()
            for i in range(q_size):
                curr = queue.get()
                if i == q_size - 1:
                    self.answer.append(curr.val)

                neighbours = self.get_neighbours(curr)
                for neighbour in neighbours:
                    if neighbour not in visited:
                        visited[neighbour.val] = 1
                        queue.put(neighbour)


    def get_neighbours(self, root):
        if root is None:
            return []

        answer = []
        if root.left is not None:
            answer.append(root.left)

        if root.right is not None:
            answer.append(root.right)

        return answer

node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)

node_1.left = node_2
node_1.right = node_3

node_2.right = node_5

node_3.right = node_4

solution = Solution()
print(solution.rightSideView(node_1))
