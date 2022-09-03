from typing import *


class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_int = "".join(reversed(n))
        return int(reversed_int, 2)

n = "00000010100101000001111010011100"
solution = Solution()
print(solution.reverseBits(n))