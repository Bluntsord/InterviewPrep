from typing import *
from functools import lru_cache

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp_grid = [set() for _ in range(len(s))]

        answer = set()
        for j in range(len(s)):
            dp_grid[j].add(s[j])
            answer.add(s[j])


        for i in range(1, len(s)):
            new_dp_arr = [set() for _ in range(len(s))]
            for j in range(len(s)):
                for k in range(j + 1, len(s)):
                    curr = dp_grid[k]
                    for word in curr:
                        next_word = s[j] + word
                        new_dp_arr[j].add(next_word)
                        answer.add(next_word)


            dp_grid = new_dp_arr

        return len(answer)

solution = Solution()
s = "aba"
print(solution.distinctSubseqII(s))


