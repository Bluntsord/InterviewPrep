from typing import *

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        m, n = destination[0] + 1, destination[1] + 1
        dp_grid = [set() for _ in range(n)]
        dp_grid[0].add("")

        right, vert = "H", "V"
        for i in range(1, n):
            dp_grid[i].add(right)
            right += "H"

        for i in range(1, m):
            next_dp_grid = [set() for _ in range(n)]
            starting_vert = {"V" * i}
            for j in range(1, n):
                up = dp_grid[j]
                left = next_dp_grid[j - 1] if j > 1 else starting_vert
                for instructions in up:
                    next_dp_grid[j].add(instructions + "V")

                for instructions in left:
                    next_dp_grid[j].add(instructions + "H")
            dp_grid = next_dp_grid

        final_instructions = list(dp_grid[n - 1])
        final_instructions.sort()
        return final_instructions[k - 1]



solution = Solution()
destination = [2,3]
k = 1
print(solution.kthSmallestPath(destination, k))

