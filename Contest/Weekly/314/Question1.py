from typing import *

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_employee, max_time = logs[0]
        for i in range(1, len(logs)):
            time_worked = logs[i][1] - logs[i - 1][1]
            if time_worked > max_time:
                max_employee, max_time = logs[i][0], time_worked
            elif time_worked == max_time:
                max_employee = min(logs[i][0], max_employee)
        return max_employee

solution = Solution()
n = 10
logs = [[0,3],[2,5],[0,9],[1,15]]
print(solution.hardestWorker(n, logs))
