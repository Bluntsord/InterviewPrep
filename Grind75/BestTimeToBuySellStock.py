import typing

class Solution:
    memo = {}
    def maxProfit(self, prices: typing.List[int]) -> int:
        return self.dp(0, prices, 1)

    def dp(self, pointer, prices, isBuy):
        if pointer >= len(prices):
            return -1
        elif pointer in self.memo:
            return self.memo[pointer]

        curr = prices[pointer]
        transact = -curr if isBuy == 1 else tr

