# Definition for a binary tree node.
from queue import Queue


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = Queue()
        queue.put(root)
        answer = []
        visited = {}

        while not queue.empty():
            curr_level = []
            for i in queue.qsize():
                curr_node = queue.get()
                curr_level.append(curr_node)
                neighbours = self.get_neighbours(curr_node)
                for neighbour in neighbours:
                    if neighbour not in visited:
                        visited[neighbour] = 1
                        queue.put(neighbour)
            answer.append(curr_level)
        return answer

    def get_neighbours(self, root):
        if root is None:
            return None
        elif root.left is None and root.right is None:
            return []
        elif root.left is None:
            return [root.left]
        elif root.right is None:
            return [root.right]
        return [root.left, root.right]

