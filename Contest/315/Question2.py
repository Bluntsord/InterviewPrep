from typing import *

nums = [1,13,10,12,31]


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        another_arr = []
        for num in nums:
            curr = int(str(num)[::-1])
            another_arr.append(curr)
        nums.extend(another_arr)
        answer = set()
        for num in nums:
            answer.add(num)

        return len(answer)

solution = Solution()
print(solution.countDistinctIntegers(nums) == 6)