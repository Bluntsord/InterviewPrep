import math
from bisect import bisect_left
from typing import *


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        first_ptr = bisect_left(arr, x) - 1
        second_ptr = first_ptr + 1
        while second_ptr - first_ptr - 1 < k:
            if first_ptr == -1:
                second_ptr += 1
                continue
            if second_ptr == len(arr) or abs(arr[first_ptr] - x) <= abs(arr[second_ptr] - x):
                first_ptr -= 1
            else:
                second_ptr += 1
        return arr[first_ptr + 1:second_ptr]



    def binary_search(self, low, high, target):
        while low <= high:
            mid = math.floor((low + high)/2)
            curr = self.arr[mid]
            if curr == target:
                return mid
            elif curr < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

arr1 = [0,0,1,2,3,3,4,7,7,8]
k1 = 3
x1 = 5
answer1 = [3, 3, 4]

arr2 = [1,2,3,4,5]
k2 = 4
x2 = -1
answer2 = [1, 2, 3, 4]

arr3 = [1,1,1,10,10,10]
k3 = 1
x3 = 9
answer3 = [10]

solution = Solution()
print(solution.findClosestElements(arr1, k1, x1) == answer1)
print("==========================================")
print(solution.findClosestElements(arr2, k2, x2) == answer2)
print("==========================================")
print(solution.findClosestElements(arr3, k3, x3) == answer3)
