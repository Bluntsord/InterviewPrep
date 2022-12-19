from typing import *
import queue as q

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        queue = q.Queue()
        self.grid = grid
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        goal = set()
        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0:
            return 0

        self.m, self.n = m, n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    start = (i, j)
                    break

        queue.put(start)
        level = 0
        visited = set()
        while not queue.empty():
            level += 1
            for i in range(queue.qsize()):
                curr_node = queue.get()
                if grid[curr_node[0]][curr_node[1]] == "#":
                    return level - 1

                neighbours = self.get_neighbours(curr_node, directions)

                for neighbour in neighbours:
                    if neighbour in visited:
                        continue

                    visited.add(neighbour)
                    queue.put(neighbour)

        return -1


    def get_neighbours(self, coord, directions):
        answer = map(lambda x: (x[0] + coord[0], x[1] + coord[1]), directions)
        answer = filter(self.valid_square, answer)

        return answer


    def valid_square(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        elif self.grid[coord[0]][coord[1]] == "X":
            return False
        return True





grid = [["O","*"],["#","O"]]

solution = Solution()
print(solution.getFood(grid))