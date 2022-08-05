from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.memo = {}
        return self.dp(amount)

    def dp(self, amount):
        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        elif amount in self.memo:
            return self.memo[amount]

        min_coins = float('inf')
        for coin in self.coins:
            temp = self.dp(amount - coin)
            if temp < 0:
                continue
            min_coins = min(min_coins, 1 + self.dp(amount - coin))

        self.memo[amount] = min_coins
        return min_coins if min_coins != float('inf') else -1

coins = [1,2,5]
amount = 11
solution = Solution()
print(solution.coinChange(coins, amount))