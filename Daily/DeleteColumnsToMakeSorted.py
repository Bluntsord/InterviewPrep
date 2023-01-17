from typing import *

class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        m, n = len(strs), len(strs[0])
        answer = 0
        for i in range(n):
            curr_string = ""
            for j in range(m):
                curr_string += strs[j][i]
            sorted_string = sorted(curr_string[:])
            answer += 1 if "".join(sorted_string) != curr_string else 0

        return answer

solution = Solution()
strs = ["abc", "bce", "cae"]
print(solution.minDeletionSize(strs))
