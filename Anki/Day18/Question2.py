from typing import *


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        for j in range(min(list(map(len,strs)))):
            curr_prefix = strs[0][j]
            for i in range(1, len(strs)):
                if curr_prefix != strs[i][j]:
                    return answer
            answer += curr_prefix
        return answer