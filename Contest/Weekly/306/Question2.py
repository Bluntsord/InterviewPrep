from typing import *

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        num_dict = {}
        for i in range(len(edges)):
            num_dict[edges[i]] = num_dict.get(edges[i], 0) + i

        print(num_dict)
        max_key, max_value = 0, 0
        for key, value in num_dict.items():
            if value > max_value:
                max_value = value
                max_key = key
            if value == max_value:
                max_key = min(max_key, key)

        return max_key
edges = [2, 0, 0, 2]
solution = Solution()
print(solution.edgeScore(edges))
