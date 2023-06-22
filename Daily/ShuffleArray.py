from typing import *


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        def translate(i, n):
            '''
            i: idx
            n: elements n
            Ret: new idx(new location) after shuffle
            '''
            if i < n:
                return 2 * i

            else:
                return 2 * i - 2 * n + 1

        if len(nums) <= 2:
            return nums

        for i in range(0, len(nums)):
            j = i
            while (nums[i] > 0):
                j = translate(j, n)
                # Mark the numbers that are at their right location negative
                nums[i], nums[j] = nums[j], -nums[i]

        for i in range(0, len(nums)):
            nums[i] = abs(nums[i])

        return nums

solution = Solution()
nums = [2,5,1,3,4,7]
n = 3
print(solution.shuffle(nums, n))

