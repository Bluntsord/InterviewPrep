from typing import *

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.min = max(weights)
        self.weights, self.days = weights, days
        left_pointer, right_pointer = self.min, sum(weights)

        while left_pointer < right_pointer:
            mid = int((left_pointer + right_pointer) // 2)
            if self.canComplete(mid):
                right_pointer = mid
            else:
                left_pointer = mid + 1

        return left_pointer

    def canComplete(self, capacity):
        if capacity < self.min:
            return False

        acc = self.weights[0]
        days = 1
        for i in range(1, len(self.weights)):
            if days > self.days:
                return False
            curr = self.weights[i]

            if acc + curr > capacity:
                acc = curr
                days += 1
            else:
                acc += curr

        return days <= self.days

weights = [1,2,3,1,1]
days = 4
solution = Solution()
print(solution.shipWithinDays(weights, days))
# print(solution.canComplete(15))