# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        cloned_node = Node(node.val)
        visited = {node: cloned_node}
        stack = [node]


        while len(stack) != 0:
            curr_node = stack.pop()
            curr_cloned_node = visited[curr_node]
            # Do the connecting
            for neighbour in curr_node.neighbors:
                if neighbour not in visited:
                    visited[neighbour] = Node(neighbour.val, [])
                    stack.append(neighbour)
                curr_cloned_node.neighbors.append(visited[neighbour])
        return visited[node]







