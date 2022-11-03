from typing import *


class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        n_arr = [int(char) for char in str(n)]
        acc, start = 0, -1
        for i in range(len(n_arr)):
            if acc + n_arr[i] > target:
                start = i
                break
            acc += n_arr[i]

        if start == -1:
            return 0

        if len(str(n)[:start]) != 0 and self.sum_digits(self.sum_digits(int(str(n)[:start]) + 1)) <= target:
            while self.sum_digits(int(str(n)[:start]) + 1) > target:
                start -= 1

            return 10 ** (len(n_arr) - start) - int(str(n)[start:])

        return 10 ** len(n_arr) - n

    def sum_digits(self, number):
        n_arr = [int(char) for char in str(number)]
        answer = sum(n_arr)

        return answer


solution = Solution()
n = [16, 467, 1, 8, 839, 19, 15]
target = [6, 6, 1, 2, 11, 1, 2]
answer = [4, 33, 0, 2, 61, 81, 5]
for i in range(len(n)):
    print(solution.makeIntegerBeautiful(n[i], target[i]) == answer[i])
#
n = 615024862295
target = 7
print(solution.makeIntegerBeautiful(n, target))