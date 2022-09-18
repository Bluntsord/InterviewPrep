from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        left_pointer, right_pointer = 0, 0
        first_max = max(nums[:k])
        second_highest = max(nums[:k], key= lambda x: x != first_max)
        for i in range(k):
            if first_max == nums[i]:
                left_pointer = i
            if second_highest == nums[i]:
                right_pointer = i

        answer = [first_max]
        for i in range(len(nums) - k):
            to_add = i + k
            if nums[to_add] > nums[left_pointer]:
                left_pointer = to_add
                right_pointer = left_pointer
            elif nums[to_add] > nums[right_pointer]:
                right_pointer = to_add

            if left_pointer < i and right_pointer < i:
                left_pointer = right_pointer = i
            elif left_pointer < i:
                left_pointer = right_pointer
            answer.append(nums[left_pointer])

        return answer

nums = [1,3,-1,-3,5,3,6,7]
k = 3
nums2 = [1, -1]
k2 = 1
solution = Solution()
print(solution.maxSlidingWindow(nums2, k2))


