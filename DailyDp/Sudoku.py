import queue


class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.processed = False
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        self.memo = {}
        for i in range(self.m):
            row_key = str(i) + "r"
            col_key = str(i) + "c"

            self.memo[row_key] = {}
            self.memo[col_key] = {}

        self.queue = queue.Queue()
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] != ".":
                    continue
                curr = (i, j)
                self.queue.put(curr)
        self.backTracking(board)
        return self.board

    def backTracking(self, board):
        if self.processed:
            return self.board
        elif self.queue.empty():
            self.processed = True
            return self.board

        while not self.queue.empty():
            assigned = False
            curr = self.queue.get()
            curr_row, curr_col = str(curr[0]) + "r", str(curr[1]) + "c"
            curr_row_dict, curr_col_dict = self.memo[curr_row], self.memo[curr_col]
            for i in range(1, 10):
                if i not in curr_row_dict and i not in curr_col_dict:
                    assigned = True
                    curr_row_dict[i] = 1
                    curr_col_dict[i] = 1
                    self.board[curr[0]][curr[1]] = str(i)

                    self.backTracking(board)

                    curr_row_dict.pop(i)
                    curr_col_dict.pop(i)
                    self.board[curr[0]][curr[1]] = "."
            if not assigned:
                self.queue.put(curr)


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
solution = Solution()
print(solution.solveSudoku(board))