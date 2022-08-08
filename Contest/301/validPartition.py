from typing import *

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        self.memo = {}
        self.nums = nums
        answer = self.dp(0)
        return answer

    def dp(self, pointer):
        if pointer == len(self.nums):
            return True
        elif pointer == len(self.nums) - 1:
            return False
        elif pointer in self.memo:
            return self.memo[pointer]

        check_2 = self.check_next_2(pointer) and self.dp(pointer + 2)
        check_3 = self.check_next_3(pointer) and self.dp(pointer + 3)
        answer = check_2 or check_3
        self.memo[pointer] = answer

        return answer

    def check_next_2(self, pointer):
        if len(self.nums) - pointer < 2 or self.nums[pointer] != self.nums[pointer + 1]:
            return False
        return True

    def check_next_3(self, pointer):
        return self.check_equal_3(pointer) or self.check_consec_3(pointer)

    def check_equal_3(self, pointer):
        if len(self.nums) - pointer < 3:
            return False
        elif self.nums[pointer] == self.nums[pointer + 1] and self.nums[pointer] == self.nums[pointer + 2]:
            return True
        return False

    def check_consec_3(self, pointer):
        if len(self.nums) - pointer < 3:
            return False
        elif self.nums[pointer] == self.nums[pointer + 1] - 1 and self.nums[pointer] == self.nums[pointer + 2] - 2:
            return True
        return False

nums = [4,4,4,5,6]
nums = [1,1,1,2]
solution = Solution()
print(solution.validPartition(nums))