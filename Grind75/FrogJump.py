from typing import *
from collections import defaultdict

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        adj_list = defaultdict(set)
        adj_list[stones[0]].add(1)

        for i in range(0, len(stones)):
            curr = stones[i]
            print("curr is", curr, adj_list[curr])
            for jump_length in adj_list[curr]:
                adj_list[curr + jump_length].add(jump_length + 1)
                adj_list[curr + jump_length].add(jump_length)
                if jump_length > 1:
                    adj_list[curr + jump_length].add(jump_length - 1)
        return len(adj_list[stones[-1]]) != 0

solution = Solution()
# stones = [0,1,3,5,6,8,12,17]
stones = [0,1,2,3,4,8,9,11]
print(solution.canCross(stones))