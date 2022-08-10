from typing import *


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        self.memo = {}
        self.arr = arr
        answer = self.dp(0)

        return answer

    def dp(self, pointer):
        pass