from typing import *


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)

        m, n = len(word1), len(word2)
        dp_grid = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp_grid[i][0] = i

        for j in range(n + 1):
            dp_grid[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                left = dp_grid[i][j - 1]
                up = dp_grid[i - 1][j]
                diag = dp_grid[i - 1][j - 1]
                if word1[i - 1] == word2[j - 1]:
                    dp_grid[i][j] = diag
                else:
                    dp_grid[i][j] = 1 + min(left, up, diag)

        return dp_grid[m][n]

word1 = "horse"
word2 = "ros"

# word1 = "intention"
# word2 = "execution"
solution = Solution()
print(solution.minDistance(word1, word2))

