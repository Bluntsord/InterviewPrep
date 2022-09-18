from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first_arr, second_arr = nums1, nums2
        if len(first_arr) > len(second_arr):
            first_arr, second_arr = second_arr, first_arr
        total_length = len(nums1) + len(nums2)
        half_length = total_length // 2

        left_pointer, right_pointer = 0, len(first_arr) - 1
        while True:
            mid = (left_pointer + right_pointer) // 2
            second_arr_partition = half_length - mid - 2

            first_arr_left = first_arr[mid] if mid >= 0 else float('-inf')
            first_arr_right = first_arr[mid + 1] if mid + 1 < len(first_arr) else float('inf')
            second_arr_left = second_arr[second_arr_partition] if second_arr_partition >= 0 else float('-inf')
            second_arr_right = second_arr[second_arr_partition + 1] if second_arr_partition + 1 < len(second_arr) else float('inf')

            if first_arr_left <= second_arr_right and second_arr_left <= first_arr_right:
                if total_length % 2 == 0:
                    return (min(first_arr_right, second_arr_right) + max(first_arr_left, second_arr_left)) / 2
                return min(first_arr_right, second_arr_right)
            elif first_arr_left > second_arr_right:
                right_pointer = mid - 1
            else:
                left_pointer = mid + 1

        return None

first_arr = [1, 3]
second_arr = [2]
solution = Solution()
print(solution.findMedianSortedArrays(first_arr, second_arr))
