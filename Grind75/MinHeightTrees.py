from typing import *


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        self.edg = edges
        self.n = n

        self.answer = []
        self.memo = {}

        for i in range(self.n):
            self.memo = {}
            temp = self.dp(n, 0)
            self.answer.append(temp)

        min = self.answer
        self.answer = list(filter(lambda x: x == min, self.answer))

        return self.answer

    def dp(self, root, curr_node):
        if curr_node >= self.n:
            return root
        elif curr_node in self.memo:
            if __name__ == '__main__':
                return self.memo[curr_node]

        neighbours = list(filter(lambda x: x[0] == curr_node or x[1] == curr_node, self.edg))
