from typing import *

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp_grid = []
        for i in range(len(triangle)):
            dp_grid.append([0 for i in range(i + 1)])
        dp_grid[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            curr_row = dp_grid[i]
            for j in range(len(curr_row)):
                straight_up = dp_grid[i - 1][j] if 0 <= j < len(curr_row) - 1 else float('inf')
                left_up = dp_grid[i - 1][j - 1] if 0 < j < len(curr_row) - 1 else float('inf')
                dp_grid[i][j] = triangle[i][j] + min(straight_up, left_up)

        for rows in dp_grid:
            print(rows)
        return min(dp_grid[len(triangle) - 1])

solution = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(solution.minimumTotal(triangle))
