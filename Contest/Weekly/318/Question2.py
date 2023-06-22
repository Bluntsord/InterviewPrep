from typing import *


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        acc = sum(nums[:k])
        window = dict(Counter(nums[:k]))
        max_so_far = acc if len(window) == k else 0

        for i in range(k, len(nums)):
            acc += nums[i] - nums[i - k]
            if nums[i - k] in window:
                if window[nums[i - k]] == 1:
                    window.pop(nums[i - k])
                else:
                    window[nums[i - k]] -= 1
            window[nums[i]] = window.get(nums[i], 0) + 1
            if len(window) == k:
                max_so_far = max(max_so_far, acc)

        return max_so_far

nums = [1,1,1,7,8,9]
k = 3
solution = Solution()
print(solution.maximumSubarraySum(nums, k))
