from typing import *


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target_window = dict(Counter(p))
        curr_window = dict(Counter(s[: len(p)]))
        answer = [0] if curr_window == target_window else []

        for i in range(len(s) - len(p)):
            drop, add = s[i], s[i + len(p)]
            curr_window[drop] = curr_window.get(drop, 0) - 1
            if curr_window[drop] == 0:
                curr_window.pop(drop)
            curr_window[add] = curr_window.get(add, 0) + 1
            if curr_window == target_window:
                answer.append(i - 1)

        return answer

solution = Solution()
s = "cbaebabacd"
p = "abc"
print(solution.findAnagrams(s, p))