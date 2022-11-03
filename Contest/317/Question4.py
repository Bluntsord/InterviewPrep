from typing import *

import sortedcontainers
from sortedcontainers import sortedlist

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        indexes, nums_with_index = sortedcontainers.SortedList(), [(num, i) for i, num in enumerate(nums)]
        nums_with_index.sort(key=lambda x: (x[0], -x[1]))
        answer = [-1] * len(nums)


        for i in reversed(range(len(nums_with_index))):
            curr_tuple = nums_with_index[i]
            if len(indexes) == 0:
                indexes.add(curr_tuple[1])
                continue

            insert_index = indexes.bisect_right(curr_tuple[1])
            if insert_index >= len(indexes) - 1:
                indexes.add(curr_tuple[1])
            else:
                answer[curr_tuple[1]] = nums[indexes[insert_index + 1]]
                indexes.add(curr_tuple[1])
        return answer


solution = Solution()
nums = [1,17,18,0,18,10,20,0]
nums = [2,4,0,9,6]
print(solution.secondGreaterElement(nums))
