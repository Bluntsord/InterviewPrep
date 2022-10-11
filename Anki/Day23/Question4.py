from collections import Counter
from typing import *

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_dict = {key:key * value for key, value in dict(Counter(nums)).items()}
        num_arr = [(key, value) for key, value in num_dict.items()]
        num_arr.sort(key=lambda x:x[0])
        print(num_arr)

        first, second = 0, num_arr[0][1]
        for i in range(1, len(num_arr)):
            curr = num_arr[i][1]
            if num_arr[i][0] == num_arr[i - 1][0] + 1:
                first, second = second, max(second, first + curr)
            else:
                first, second = second, curr + second

        return second

nums = [2,2,3,3,3,4]
solution = Solution()
print(solution.deleteAndEarn(nums))







