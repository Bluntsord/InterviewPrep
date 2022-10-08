from typing import *

class Solution:
    def coin_change(self, coins: list, target):
        self.memo = {}
        self.target = target
        self.coins = coins
        self.coins.reverse()
        answer = self.dp(target)

        return answer if answer != float('inf') else -1

    def dp(self, amount_left):
        if amount_left < 0:
            return float('inf')
        elif amount_left == 0:
            return 0
        elif amount_left in self.memo:
            return self.memo[amount_left]

        answer = float('inf')
        for coin in self.coins:
            answer = min(answer, 1 + self.dp(amount_left - coin))

        self.memo[amount_left] = answer
        return answer

