import bisect
from typing import *

class Solution:
    def solution(self, objects, radius):
        diameter = radius * 2
        objects.sort()
        left_pointer  = 0
        right_pointer = bisect.bisect_left(objects, objects[0] + diameter)
        answer = left_pointer - right_pointer
        for object in objects:
            next_left = object
            next_right = object + diameter
            curr = right_pointer
            pass
        pass


objects = [-5, 3, 4, 9]
radius = 5
solution = Solution()
print(solution.solution(objects, radius))
