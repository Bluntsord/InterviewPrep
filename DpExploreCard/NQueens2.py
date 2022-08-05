class Solution:
    def totalNQueens(self, n: int) -> int:
        self.threatened_row = {}
        self.threatened_col = {}
        self.threatened_diag = {}
        self.threatened_antidiag = {}
        self.answer = 0
        self.n = n
        self.backTracking(0)

        return self.answer

    def backTracking(self, row):
        if row == self.n:
            self.answer += 1
            return

        for col in range(self.n):
            curr_diag = row - col
            curr_anti_diag = row + col
            if col in self.threatened_col or \
                curr_diag in self.threatened_diag or \
                curr_anti_diag in self.threatened_antidiag:

                continue

            self.threatened_col[col] = 1
            self.threatened_diag[curr_diag] = 1
            self.threatened_antidiag[curr_anti_diag] = 1

            self.backTracking(row + 1)

            self.threatened_col.pop(col)
            self.threatened_diag.pop(curr_diag)
            self.threatened_antidiag.pop(curr_anti_diag)

        return

solution = Solution()
print(solution.totalNQueens(4))

