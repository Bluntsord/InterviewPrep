from typing import *


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        acc = answer = 0
        for num in nums:
            acc += num
            acc = acc % k
            answer += prefix_sum.get(acc, 0)
            prefix_sum[acc] = prefix_sum.get(acc, 0) + 1

        return answer


nums = [4,5,0,-2,-3,1]
k = 5
solution = Solution()
print(solution.subarraysDivByK(nums, k))