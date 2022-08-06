from typing import *

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sorted_heights = sorted(heights)
        answer = 0
        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                answer += 1

        return answer
