cost = [1,100,1,1,1,100,1,1,100,1]


class Solution(object):
    memo = {}
    def minCostClimbingStairs(self, cost):
        cost.insert(0, 0)
        temp_cost = cost
        return self.dp(0, temp_cost)

    def dp(self, pointer, cost):
        if pointer >= len(cost):
            return 0
        elif pointer in self.memo:
            return self.memo[pointer]

        current_step_cost = cost[pointer]
        take_one = current_step_cost + self.dp(pointer + 1, cost)
        take_two = current_step_cost + self.dp(pointer + 2, cost)

        answer = min(take_one, take_two)
        self.memo[pointer] = answer

        return answer

solution = Solution()
print(solution.minCostClimbingStairs(cost))
