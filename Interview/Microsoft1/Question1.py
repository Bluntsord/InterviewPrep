from typing import *


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] > rec2[0] or rec1[1] > rec2[1]:
            rec1, rec2 = rec2, rec1
        top_rec1, btm_rec1 = (rec1[0], rec1[1]), (rec1[2], rec1[3])
        top_rec2, btm_rec2 = (rec2[0], rec2[1]), (rec2[2], rec2[3])

        if btm_rec1[0] > top_rec2[0] and btm_rec1[1] > top_rec2[1]:
            return True
        return False

rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
rec3 = [0,0,1,1]
rec4 = [1,0,2,1]
solution = Solution()
print(solution.isRectangleOverlap(rec3, rec4))
