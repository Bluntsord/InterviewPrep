from typing import *


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = set(nums)
        answer = 0
        for num in nums_dict:
            if num - 1 not in nums_dict:
                curr = num
                curr_max = 1

                while curr + 1 in nums_dict:
                    curr = curr + 1
                    curr_max += 1
                answer = max(answer, curr_max)
        return answer



nums = [100, 4, 200, 1, 3, 2]
nums2 = [100, 3, 200, 1, 4, 2]

solution = Solution()
print(solution.longestConsecutive(nums))


