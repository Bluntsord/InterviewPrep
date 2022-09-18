from typing import *


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        num_dict = dict(Counter(nums))
        max_number, occurrences = -1, 0
        for key, value in num_dict.items():
            if key % 2 == 0 and value == occurrences:
                max_number = min(max_number, key)
            elif key % 2 == 0 and value > occurrences:
                max_number = key
                occurrences = value

        return max_number

solution = Solution()
nums = [0,1,2,2,4,4,1]
print(solution.mostFrequentEven(nums))