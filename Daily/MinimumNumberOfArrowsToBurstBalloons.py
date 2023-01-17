from typing import *

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        answer = 0
        stack = [points[0]]
        print(points)

        for point in points[1:]:
            if stack[-1][1] >= point[0]:
                stack[-1] = [stack[-1][0], min(stack[-1][1], point[1])]
            else:
                answer += 1
                stack[-1] = point

        answer += 1
        return answer


points = [[10,16],[2,8],[1,6],[7,12]]
solution = Solution()
print(solution.findMinArrowShots(points))