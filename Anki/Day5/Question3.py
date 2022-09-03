from typing import *


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_dict = dict(Counter(s[:len(p)]))
        target_dict = dict(Counter(p))
        answer = [0] if window_dict == target_dict else []

        for i in range(len(s) - len(p)):
            drop = s[i]
            take = s[i + len(p)]
            window_dict[drop] -= 1
            if window_dict[drop] == 0: window_dict.pop(drop)
            window_dict[take] = window_dict.get(take, 0) + 1
            print(window_dict)
            if window_dict == target_dict: answer.append(i + 1)

        return answer

s = "cbaebabacd"
p = "abc"
solution = Solution()
print(solution.findAnagrams(s, p))


