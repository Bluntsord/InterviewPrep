from typing import *


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        task_dict = {}
        answer = 0
        for i in range(len(tasks)):
            curr_task = tasks[i]
            if curr_task not in task_dict:
                answer += 1
            elif curr_task in task_dict and answer - task_dict[curr_task] > space:
                answer += 1
            else:
                answer = task_dict[curr_task] + space + 1
            task_dict[curr_task] = answer

        return answer

tasks = [1,2,1,2,3,1]
space = 3
solution = Solution()
print(solution.taskSchedulerII(tasks, space))