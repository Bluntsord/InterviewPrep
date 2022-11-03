from typing import *


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        intersect = set(mat[0])
        for curr in mat[1:]:
            curr_set = set(curr)
            intersect = intersect & curr_set

        return min(intersect)

solution = Solution()
mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
print(solution.smallestCommonElement(mat))