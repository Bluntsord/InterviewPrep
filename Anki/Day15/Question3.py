from typing import *
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_set, row_set, square_set = defaultdict(set), defaultdict(set), defaultdict(set)
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                curr_value = board[i][j]
                current_square = (i // 3) + 3 * (j // 3)
                if curr_value in row_set[i] or curr_value in column_set[j] \
                        or curr_value in square_set[current_square]:
                    return False
                row_set[i].add(curr_value)
                column_set[j].add(curr_value)
                square_set[current_square].add(curr_value)

        return True