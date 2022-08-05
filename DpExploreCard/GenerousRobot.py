class Solution(object):
    def __init__(self):
        self.robots = {"common": 5, "rare": 0, "epic": 1, "legend": 0}
        self.memo = {}
        self.rate = {"common": 7, "rare": 10, "epic": 15, "legend": 40}

    def most_gear(self, num_of_days):
        total = 0
        for key in self.robots:
            temp = self.robots[key] * self.staking(key, num_of_days)
            total += temp
        return total

    def staking(self, rarity, days):
        if days < 12:
            return 0

        base = self.rate[rarity] * days
        if days < 20:
            return base
        elif days < 30:
            return base * 1.25
        elif days < 60:
            return base * 1.5
        return base * 2

solution = Solution()
days = 60
print(solution.most_gear(days) * 1 * 1.37/days)