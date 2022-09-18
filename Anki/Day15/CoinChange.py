from typing import *


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo, self.coins = {}, coins
        return self.dp(amount)

    def dp(self, amount_left):
        if amount_left < 0:
            return float('inf')
        elif amount_left == 0:
            return 0
        elif amount_left in self.memo:
            return self.memo[amount_left]

        answer = 0
        for coins in reversed(self.coins):
            answer = min(answer, 1 + self.dp(amount_left - coins))

        self.memo[amount_left] = answer
        return answer


