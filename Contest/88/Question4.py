from typing import *


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        value_arr = [(i, nums1[i] - nums2[i]) for i in range(len(nums1))]
        value_arr.sort(key=lambda x: x[1])
        left_pointer, right_pointer = 0, len(nums1) - 1
        answer = 0
        while left_pointer <= right_pointer:
            if value_arr[right_pointer][1] - value_arr[left_pointer][1] > diff:
                left_pointer += 1
            else:
                answer += 1
                right_pointer -= 1

        return answer

nums1 = [3,2,5]
nums2 = [2,2,1]
diff = 1
solution = Solution()
print(solution.numberOfPairs(nums1, nums2, diff))



