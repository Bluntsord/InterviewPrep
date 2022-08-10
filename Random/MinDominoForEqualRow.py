from typing import *


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        zipped = list(zip(tops, bottoms))
        acc = {i for i in range(7)}

        for domino in zipped:
            curr_domino_set = {domino[0], domino[1]}
            acc = acc.intersection(curr_domino_set)

        if len(acc) == 0:
            return -1

        answer = float('inf')
        for target in acc:
            top = 0
            btm = 0
            for domino in zipped:
                if domino[0] != target:
                    top += 1
                if domino[1] != target:
                    btm += 1
            curr = min(top, btm)
            answer = min(answer, curr)

        return answer

solution = Solution()
tops = [6,1,6,4,6,6]
bottoms = [5,6,2,6,3,6]
print(solution.minDominoRotations(tops, bottoms))
