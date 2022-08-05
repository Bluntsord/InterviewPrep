import time

coins = [1,2,5, 7, 10, 12, 17, 20]
amount = 993


class Solution(object):
    memo = {}
    counter = 0
    def coinChange(self, coins, amount):
        start_time = time.time()
        memo = {}

        # Heuristic to use the bigger coins first
        coins.sort(reverse=True)
        print(coins)


        answer = self.dp(coins, amount)
        print("--- %s seconds ---" % (time.time() - start_time))
        print(self.counter)
        return answer

    def dp(self, coins, amount):
        self.counter += 1
        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        elif amount in self.memo:
            return self.memo[amount]

        answer = float('inf')
        for coin in coins:
            coins_left = self.dp(coins, amount - coin)
            answer = min(answer, 1 + coins_left) if coins_left >= 0 else float('inf')

        self.memo[amount] = answer

        return answer


solution = Solution()
print(solution.coinChange(coins, amount))