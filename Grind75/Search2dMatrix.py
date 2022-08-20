import bisect
from typing import *

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.m = len(matrix)
        self.n = len(matrix[0])
        first_col = []
        for i in range(self.m):
            first_col.append(matrix[i][0])
        row = bisect.bisect_left(first_col, target)
        if row < self.m:
            row -= 0 if matrix[row][0] == target else 1
        elif row == self.m:
            row -= 1
        row_of_ints = matrix[row]
        print(row_of_ints)
        col = bisect.bisect_left(row_of_ints, target)
        if col < self.n:
            col -= 0 if row_of_ints[col] == target else 1
        elif col == self.n:
            col -= 1
        print(row)
        print(col)
        return matrix[row][col] == target

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# matrix = [[1]]
# temp = [1, 10, 23]
# print(bisect.bisect_left(temp, 10))
target = 5
solution = Solution()
print(solution.searchMatrix(matrix, target))


