from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices, self.memo = prices, {}
        return self.dp(0, 2, True)

    def dp(self, pointer, transactions_left, is_buy):
        key = (pointer, transactions_left, is_buy)
        if pointer >= len(self.prices) or transactions_left == 0:
            return 0
        elif key in self.memo:
            return self.memo[key]

        curr = self.prices[pointer]
        if is_buy:
            take_curr = -curr + self.dp(pointer + 1, transactions_left, False)
        else:
            take_curr = curr + self.dp(pointer + 1, transactions_left - 1, True)

        drop_curr = self.dp(pointer + 1, transactions_left, is_buy)
        answer = max(drop_curr, take_curr)
        self.memo[key] = answer

        return answer

solution = Solution()
prices = [1, 2, 3, 4, 5]
print(solution.maxProfit(prices))