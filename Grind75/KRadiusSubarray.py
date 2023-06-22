from typing import *

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        window_sum = 0
        leg = k * 2 + 1

        for i in range(min(leg, len(nums))):
            window_sum += nums[i]
        answer = []

        for i in range(len(nums)):
            if i < k or i >= len(nums) - k:
                answer.append(-1)
                continue

            left, right = i - k, i + k + 1
            print(window_sum)
            curr = window_sum // ((k * 2) + 1)
            answer.append(curr)
            window_sum -= nums[left]
            window_sum += nums[right] if right < len(nums) else 0

        return answer

nums = [7,4,3,9,1,8,5,2,6]
k = 3
solution = Solution()
print(solution.getAverages(nums, k))



