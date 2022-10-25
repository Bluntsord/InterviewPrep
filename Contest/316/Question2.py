from typing import *


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        base, left_pointer, right_pointer = -1, 0, 0
        curr_gcd = None
        answer = 0
        while right_pointer < len(nums):
            if nums[right_pointer] % k != 0:
                temp = right_pointer + 1
                left_pointer = right_pointer = temp
                continue
            curr_gcd = self.euclid_formula(curr_gcd, nums[right_pointer]) if curr_gcd is not None else nums[right_pointer]

            while right_pointer + 1 < len(nums) and self.euclid_formula(curr_gcd, nums[right_pointer + 1]) == k:
                curr_gcd = self.euclid_formula(curr_gcd, nums[right_pointer + 1])
                temp = nums[right_pointer + 1]
                right_pointer += 1

            answer += (right_pointer - left_pointer + 1) if curr_gcd == k else 0
            right_pointer = right_pointer + 1

        return answer

    def euclid_formula(self, first, second):
        first = first if first < second else second
        second = second if first < second else first

        while second != 0:
            temp = second
            second = first % second
            first = temp

        return first

solution = Solution()
nums = [3,12,9,6]
k = 3
# nums = [4]
# k = 4
# print(solution.euclid_formula(4, 8))
print(solution.subarrayGCD(nums, k))

