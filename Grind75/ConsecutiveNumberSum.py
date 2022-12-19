import bisect
from typing import *

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        counter = 0
        for i in range(1, n):
            curr = n - self.ap_formula(1, i)
            if curr < 1:
                continue
            elif (n - self.ap_formula(1, i)) % (i + 1) == 0:
                counter += 1

        return counter + 1
    # def consecutiveNumbersSum(self, n: int) -> int:
    #     counter = 0
    #     for i in range(1, n):
    #         curr = self.binary_search(i, n, 0, n)
    #         if curr != -1:
    #             counter += 1
    #
    #     return counter + 1
    #
    def ap_formula(self, start, num):
        return (num / 2) * (2 * start + (num - 1))

        counter = 0
    #
    # def binary_search(self, start, target, low, high):
    #     while low < high:
    #         mid = (low + high) // 2
    #         curr_value = self.ap_formula(start, mid)
    #         if curr_value == target:
    #             return mid
    #         elif curr_value < target:
    #             low = mid + 1
    #         else:
    #             high = mid
    #
    #     return -1

def num_consecutive_sums(n):
  count = 0
  k = 1
  while k <= n:
    if n % k == 0:
      if n / k >= k:
        count += 1
    k += 1
  return count + 1

n = 15
print(num_consecutive_sums(n))
# solution = Solution()
# print(solution.consecutiveNumbersSum(20))


