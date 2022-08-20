from typing import *


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        acc = 0
        answer = 0

        for num in nums:
            acc += num
            diff = acc - k

            answer += prefix_count.get(diff, 0)
            prefix_count[acc] = 1 + prefix_count.get(diff, 0)

        return answer

nums = [1]
k = 0

nums2 = [5,3,7,1,3,4]
k2 = 8
solution = Solution()
print(solution.subarraySum(nums, k))
# print(solution.subarraySum(nums2, k2))



