from typing import *


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_dict = {heights[i]: names[i] for i in range(len(heights))}
        heights.sort(reverse=True)
        answer = list(map(lambda x: height_dict[x], heights))
        return answer

names = ["Mary","John","Emma"]
heights = [180,165,170]
solution = Solution()
print(solution.sortPeople(names, heights))