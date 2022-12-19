from typing import *
from math import comb


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        self.memo = {}
        self.lcm_memo = {}
        self.nums = nums
        answer = 0
        if len(nums) == 1:
            return 1 if self.lcm(nums[0], 1) == k else 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                lcm = self.lcm_pointer(i, j)
                if k % lcm != 0:
                    break
                print(i, j, lcm)
                answer += 1 if int(lcm) == k else 0

        return answer

    # def subarrayLCM(self, nums: List[int], k: int) -> int:
    #     self.memo = {}
    #     left_pointer, right_pointer = 0, 0
    #
    #     answer = 0
    #     while right_pointer < len(nums):
    #         k_count = 0
    #         window_lcm = nums[left_pointer]
    #         while right_pointer < len(nums) and k % nums[right_pointer] == 0:
    #             k_count += 1 if nums[right_pointer] == k else 0
    #             window_lcm = self.lcm(window_lcm, nums[right_pointer])
    #             right_pointer += 1
    #
    #         for i in range(2, right_pointer - left_pointer + 1):
    #             answer += comb(right_pointer - left_pointer + 1, i)
    #         answer += k_count
    #
    #         right_pointer += 1
    #
    #     return answer

    def gcd(self, first, second):
        if first < second:
            first, second = second, first

        key = (first, second)
        if first == 0 or second == 0:
            return first if first != 0 else 1
        elif key in self.memo:
            return self.memo[key]

        answer = self.gcd(second, first % second)
        self.memo[key] = answer

        return answer

    def lcm(self, first, second):
        if first == second:
            return first
        return (first * second)/ self.gcd(first, second)

    def lcm_pointer(self, left_pointer, right_pointer):
        key = (left_pointer, right_pointer)
        if left_pointer == right_pointer:
            return self.nums[left_pointer]
        elif key in self.lcm_memo:
            return self.lcm_memo[key]

        previous = self.lcm_pointer(left_pointer, right_pointer - 1)
        answer = self.lcm(previous, self.nums[right_pointer])

        self.memo[key] = answer

        return answer



# solution = Solution()
# nums = [3, 6, 2, 7, 1]
# k = 6
# print(solution.subarrayLCM(nums, k))
# print("lcm is: ", solution.lcm(6, 7))
n = 10
arr = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j] = 2
        elif abs(i - j) == n - 1:
            arr[i][j] = 1
        else:
            arr[i][j] = 0

for row in arr:
    print(row)

