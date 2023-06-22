from typing import *


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        acc = 0
        for i in range(len(nums1)):
            curr = 0 if len(nums2) % 2 == 0 else nums1[i]
            acc ^= curr

        for i in range(len(nums2)):
            curr = 0 if len(nums1) % 2 == 0 else nums2[i]
            acc ^= curr

        return acc

nums1 = [2,1,3]
nums2 = [10,2,5,0]

# nums1 = [1,2]
# nums2 = [3,4]
solution = Solution()
print(solution.xorAllNums(nums1, nums2))