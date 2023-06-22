from typing import *

# a + b = a ^ b + 2* a & b
# a + b - 2* a & b = a ^ b

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        acc = pref[0]
        answer = [acc]
        for i in range(1, len(pref)):
            acc = pref[i] ^ pref[i - 1]
            answer.append(acc)
        return answer

solution = Solution()
pref = [5,2,0,3,1]
print(solution.findArray(pref))
