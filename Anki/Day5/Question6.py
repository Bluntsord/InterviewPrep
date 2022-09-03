from typing import *


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = dict(Counter(s[:len(p)]))
        target_window = dict(Counter(p))
        answer = [0] if window == target_window else []

        for i in range(len(s) - len(p)):
            drop = s[i]
            take = s[i + len(p)]
            window[drop] -= 1
            if window[drop] == 0: window.pop(drop)
            window[take] = window.get(take, 0) + 1
            if window == target_window: answer.append(i + 1)

        return answer
