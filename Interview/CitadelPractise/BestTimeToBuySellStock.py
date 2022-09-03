from typing import *


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        self.k = k
        self.prices = prices
        self.memo = {}
        return self.dp(k, 0, True)

    def dp(self, transactions_left, pointer, is_buy):
        key = str(transactions_left) + "|" + str(pointer) + "|"  + str(is_buy)
        if pointer >= len(self.prices):
            return 0
        elif transactions_left <= 0:
            return 0
        elif key in self.memo:
            return self.memo[key]

        curr = self.prices[pointer]
        if is_buy:
            take_curr = -curr + self.dp(transactions_left, pointer + 1, False)
        else:
            take_curr = curr + self.dp(transactions_left - 1, pointer + 1, True)
        drop_curr = self.dp(transactions_left, pointer + 1, is_buy)
        answer = max(take_curr, drop_curr)
        self.memo[key] = answer

        return answer

k = 2
prices = [2,4,1]
solution = Solution()
print(solution.maxProfit(k, prices))
