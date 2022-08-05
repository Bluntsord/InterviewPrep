from typing import *

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_dict = []
        row_dict = []
        square_dict = []
        for i in range(0, 9):
            curr_col_dict = {}
            curr_row_dict = {}
            curr_square_dict = {}
            col_dict.append(curr_col_dict)
            row_dict.append(curr_row_dict)
            square_dict.append(curr_square_dict)

        self.m = len(board)
        self.n = len(board[0])

        for i in range(self.m):
            for j in range(self.n):
                curr = board[i][j]
                if curr == ".":
                    continue

                curr_row_dict = row_dict[i]
                curr_col_dict = col_dict[j]
                curr_square_dict = square_dict[(i // 3) * 3 + (j // 3)]
                if curr in curr_row_dict or curr in curr_col_dict:
                    return False
                curr_row_dict[curr] = 1
                curr_col_dict[curr] = 1
                curr_square_dict[curr] = 1

        return True

board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]

solution = Solution()
print(solution.isValidSudoku(board))