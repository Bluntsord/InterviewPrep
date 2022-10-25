from typing import *


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num + 1):
            curr = i
            # if len(str(i)) != len(str(num)):
            #     pad = (len(str(num)) - len(str(i))) * "0"
            #     curr = pad + str(curr)
            reverse = int(str(curr)[::-1])
            if int(reverse) + int(curr) == num:
                return True
        return False

solution = Solution()
num = 10
print(solution.sumOfNumberAndReverse(num))