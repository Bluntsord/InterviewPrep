from typing import *


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        mod_arr = [num % space for num in nums]
        temp = dict(Counter(mod_arr))
        print(temp)
        max_value = max(temp.values())
        max_keys = set()
        print("max_values is ", max_value)

        for key, values in temp.items():
            if values == max_value:
                max_keys.add(key)
        print(max_keys)

        min_so_far = float('inf')
        for i in range(len(nums)):
            if mod_arr[i] in max_keys:
                min_so_far = min(min_so_far, nums[i])

        return min_so_far



solution = Solution()
nums1 = [1,3,5,2,4,6]
space1 = 2
nums = [6, 2, 5]
space = 100
print(solution.destroyTargets(nums, space))