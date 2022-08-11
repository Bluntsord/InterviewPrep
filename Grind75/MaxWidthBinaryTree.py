from typing import *
import queue as q


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = q.Queue()
        queue.put(root)
        visited = {root: 0}
        answer = 0
        counter = 1

        while not queue.empty() and counter != 0:
            curr_length = []
            counter = 0
            for i in range(queue.qsize()):
                curr_node = queue.get()
                if curr_node is not None:
                    curr_length.append(curr_node.val)
                else:
                    curr_length.append(None)

                neighbours = self.get_neighbours(curr_node)
                for neighbour in neighbours:
                    if neighbour not in visited or neighbour is None:
                        queue.put(neighbour)
                        if neighbour is not None:
                            counter += 1
                            visited[neighbour] = 1
            for i in range(len(curr_length) - 1, -1, -1):
                if curr_length[i] is not None:
                    break
            for j in range(len(curr_length)):
                if curr_length[j] is not None:
                    break
            print(curr_length)
            answer = max(answer, (i - j) + 1)
        return answer

    def get_neighbours(self, node):
        if node is None:
            return [None, None]
        answer = []
        answer.append(node.right)
        answer.append(node.left)
        return answer


first = TreeNode(1)
second = TreeNode(2)
third = TreeNode(3)
forth = TreeNode(4)
fifth = TreeNode(5)

first.left = second
first.right = third
second.left = fifth
third.right = forth

solution = Solution()
print(solution.widthOfBinaryTree(first))


