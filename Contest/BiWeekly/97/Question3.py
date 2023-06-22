import bisect
from typing import *
from collections import Counter

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        self.prize_dict = dict(Counter(prizePositions))
        self.possible_keys = sorted(self.prize_dict.keys())
        self.memo, self.k = {}, k

        acc = self.prize_dict[self.possible_keys[0]]
        self.prefix_sum = [acc]

        for i in range(1, len(self.possible_keys)):
            acc += self.prize_dict[self.possible_keys[i]]
            self.prefix_sum.append(acc)

        print(self.prefix_sum)
        return self.dp(0, 2)

    def dp(self, pointer, number_of_segments_left):
        key = (pointer, number_of_segments_left)
        if pointer >= len(self.possible_keys) or number_of_segments_left == 0:
            return 0
        elif key in self.memo:
            return self.memo[key]

        curr = self.possible_keys[pointer]
        next = curr + self.k
        next_range = bisect.bisect_right(self.possible_keys, next)
        acc = self.prefix_sum[next_range - 1] if pointer == 0 else self.prefix_sum[next_range - 1] - self.prefix_sum[pointer - 1]
        take_curr = acc + self.dp(next_range, number_of_segments_left - 1)
        drop_curr = self.dp(pointer + 1, number_of_segments_left)

        answer = max(take_curr, drop_curr)
        self.memo[key] = answer

        return answer

solution = Solution()
prizePositions = [1,1,2,2,3,3,5]
k = 2
print(solution.maximizeWin(prizePositions, k))