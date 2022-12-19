from typing import *
from functools import lru_cache

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp_dict = {}

        @lru_cache(None)
        def dp(pointer, curr_width, curr_level_height):
            key = (pointer, curr_width, curr_level_height)
            if curr_width > shelfWidth:
                return float('inf')
            elif curr_level_height >= float('inf'):
                return float('inf')
            elif pointer == len(books):
                return 0
            elif key in dp_dict:
                return dp_dict[key]

            curr_book = books[pointer]
            level_increase = max(curr_book[1] - curr_level_height, 0)
            if curr_width + curr_book[0] <= shelfWidth:
                stay_level = level_increase + dp(pointer + 1, curr_width + curr_book[0], curr_level_height + level_increase)
            else:
                stay_level = float('inf')
            new_level = curr_book[1] + dp(pointer + 1, curr_book[0], curr_book[1])
            answer = min(stay_level, new_level)

            dp_dict[key] = answer

            return answer

        return dp(0, 0, 0)

solution = Solution()
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelf_width = 4
print(solution.minHeightShelves(books, shelf_width))