from typing import List


class Solution:
    def __init__(self):
        self.row = None
        self.col = None
        self.visited = {}
        self.grid = None

    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = {}
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0])

        answer = 0
        for i in range(self.row):
            for j in range(self.col):
                curr_node = (i, j)
                answer += self.dfs(curr_node)

        return answer


    def dfs(self, coord: tuple):
        if coord in self.visited:
            return 0
        elif self.grid[coord[0]][coord[1]] == '0':
            self.visited[coord] = 1
            return 0
        stack = [coord]
        self.visited[coord] = 1

        while len(stack) != 0:
            curr = stack.pop()
            self.visited[curr] = 1
            if self.grid[curr[0]][curr[1]] == '0':
                continue
            neighbours = self.find_neighbours(curr)

            for neighbour in neighbours:
                if neighbour not in self.visited:
                    stack.append(neighbour)

        return 1



    def find_neighbours(self, coord: tuple) -> List[tuple]:
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        answer = list(map(lambda x: (coord[0] + x[0], coord[1] + x[1]), dir))
        answer = list(filter(lambda x: self.valid_coord(x), answer))
        return answer

    def valid_coord(self, coord: tuple) -> bool:
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.row or coord[1] >= self.col:
            return False
        return True

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
solution = Solution()
print(solution.numIslands(grid))