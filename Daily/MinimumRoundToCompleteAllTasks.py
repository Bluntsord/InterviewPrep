from typing import *

class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        level_dict = dict(Counter(tasks))
        answer = 0
        for key, value in level_dict.items():
            if value == 1:
                return -1
            occurrences = value % 3
            answer += value // 3 if occurrences == 0 else (value // 3) + 1


        return answer

solution = Solution()
tasks = [2,2,3,3,2,4,4,4,4,4]
print(solution.minimumRounds(tasks))