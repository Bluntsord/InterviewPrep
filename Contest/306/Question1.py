from typing import *

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        self.grid = grid
        m = len(grid)
        n = len(grid[0])
        answer = [[-1 for i in range(n - 2)] for j in range(m - 2)]
        print(answer)
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == m - 1:
                    continue
                curr_coord = (i, j)
                answer[i - 1][j - 1] = self.helper(curr_coord)

        return answer

    def helper(self, coord):
        answer = 0
        print(coord)
        for i in range(coord[0] - 1, coord[0] + 2):
            for j in range(coord[1] - 1, coord[1] + 2):
                temp = (i, j)
                print(i, j)
                curr = self.grid[i][j]
                answer = max(answer, curr)
        print("====")
        return answer

grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]

grid = [[20,8,20,6,16,16,7,16,8,10],
        [12,15,13,10,20,9,6,18,17,6],
        [12,4,10,13,20,11,15,5,17,1],
        [7,10,14,14,16,5,1,7,3,11],
        [16,2,9,15,9,8,6,1,7,15],
        [18,15,18,8,12,17,19,7,7,8],
        [19,11,15,16,1,3,7,4,7,11],
        [11,6,5,14,12,18,3,20,14,6],
        [4,4,19,6,17,12,8,8,18,8],
        [19,15,14,11,11,13,12,6,16,19]]
solution = Solution()
print(solution.largestLocal(grid))