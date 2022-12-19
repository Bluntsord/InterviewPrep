from typing import *
import queue as q

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        rows, cols = len(grid), len(grid[0])

        max_count = 0
        row_hits = 0
        col_hits = [0] * cols

        for row in range(0, rows):
            for col in range(0, cols):
                # reset the hits on the row, if necessary.
                if col == 0 or grid[row][col - 1] == 'W':
                    row_hits = 0
                    for k in range(col, cols):
                        if grid[row][k] == 'W':
                            # stop the scan when we hit the wall.
                            break
                        elif grid[row][k] == 'E':
                            row_hits += 1

                # reset the hits on the col, if necessary.
                if row == 0 or grid[row - 1][col] == 'W':
                    col_hits[col] = 0
                    for k in range(row, rows):
                        if grid[k][col] == 'W':
                            break
                        elif grid[k][col] == 'E':
                            col_hits[col] += 1

                # count the hits for each empty cell.
                if grid[row][col] == '0':
                    total_hits = row_hits + col_hits[col]
                    max_count = max(max_count, total_hits)

        return max_count


solution = Solution()
grid = [["0","E","0","0"],
        ["E","0","W","E"],
        ["0","W","0","0"],
        ["0","E","W","0"]]
print(solution.maxKilledEnemies(grid))


