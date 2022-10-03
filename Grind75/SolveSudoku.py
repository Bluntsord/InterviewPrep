from typing import *
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_dict, col_dict, square_dict = defaultdict(set)
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                curr_value = board[i][j]
                if not curr_value.isdigit():
                    continue
                curr_square = (j // 3) + 3 * (i // 3)
                row_dict[i].add(curr_value)
                col_dict[j].add(curr_value)
                square_dict[curr_square].add(curr_value)
