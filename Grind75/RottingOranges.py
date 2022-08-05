from queue import Queue
from typing import List


class Solution:
    def __init__(self):
        self.row = None
        self.col = None
        self.grid = None
        self.rottingOranges = None
        self.freshOranges = None
        self.rottingOrangesQueue = None

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.row = len(grid)
        self.col = len(grid[0])
        self.grid = grid
        self.rottingOranges = 0
        self.freshOranges = 0
        self.visited = {}
        self.rottingOrangesQueue = Queue()

        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] == 1:
                    self.freshOranges += 1
                elif self.grid[i][j] == 2:
                    self.rottingOranges += 1
                    coord = (i, j)
                    self.visited[coord] = 1
                    self.rottingOrangesQueue.put(coord)

        return self.bfs()

    def bfs(self) -> int:
        queue = self.rottingOrangesQueue
        answer = 0
        while not queue.empty():
            for i in range(queue.qsize()):
                curr = queue.get()
                neighbours = self.find_neighbours(curr)

                for neighbour in neighbours:
                    if neighbour not in self.visited:
                        curr_state = self.grid[neighbour[0]][neighbour[1]]
                        if curr_state == 1:
                            self.rottingOranges += 1
                            self.freshOranges -= 1
                            queue.put(neighbour)
                        elif curr_state == 2:
                            queue.put(neighbour)
                        self.visited[neighbour] = 1
            answer += 1

        return answer - 1 if self.freshOranges == 0 else -1


    def find_neighbours(self, coord: tuple) -> List[tuple]:
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        answer = list(map(lambda x: (coord[0] + x[0], coord[1] + x[1]), dir))
        answer = list(filter(lambda x: self.valid_coord(x), answer))
        return answer

    def valid_coord(self, coord: tuple) -> bool:
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.row or coord[1] >= self.col:
            return False
        return True




grid = [[2,1,1],[1,1,0],[0,1,1]]
grid2 = [[2,1,1],
         [0,1,1],
         [1,0,1]]
grid3 = [[0, 2]]
grid4 = [[2,0],[1,0]]
solution = Solution()
print(solution.orangesRotting(grid4))