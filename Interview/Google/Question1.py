from typing import *


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_dict = {}
        for num in arr:
            num_dict[num] = num_dict.get(num, 0) + 1
        temp = set()
        for num in num_dict.values():
            if num in temp:
                return False
            temp.add(num)
        return True


