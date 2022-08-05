from typing import *


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)

        answer = 0
        acc = 0
        for box_no, unit_per_box in boxTypes:
            if acc > truckSize:
                return answer
            elif acc + box_no <= truckSize:
                answer += (box_no * unit_per_box)
            else:
                temp = (truckSize - acc) * unit_per_box
                answer += temp
            acc += box_no

        return answer

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4

solution = Solution()
print(solution.maximumUnits(boxTypes, truckSize))