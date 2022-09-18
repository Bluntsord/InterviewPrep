from typing import *
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict, col_dict, square_dict = defaultdict(set), defaultdict(set), defaultdict(set)
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                curr_value = board[i][j]
                curr_square = (j // 3) + 3 * (i // 3)
                if curr_value in square_dict[curr_square] or curr_value in col_dict[j] or curr_value in row_dict[i]:
                    return False
                square_dict[curr_square].add(curr_value)
                col_dict[j].add(curr_value)
                row_dict[i].add(curr_value)

        return True