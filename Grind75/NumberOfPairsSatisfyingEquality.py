from typing import *
from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums3 = [nums1[i] - nums2[i] for i in range(len(nums1))]
        s1 = SortedList()
        answer = 0

        for i in range(len(nums3)):
            curr = s1.bisect_right(nums3[i] + diff)
            answer += curr
            s1.add(nums3[i])

        return answer

nums1 = [-4,-4,4,-1,-2,5]
nums2 = [-2,2,-1,4,4,3]
diff = 1

solution = Solution()
print(solution.numberOfPairs(nums1, nums2, diff))
# print(solution.binary_search(nums3, diff, 0, len(nums3), nums3[0]))