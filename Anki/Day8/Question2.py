from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.memo = {}
        self.acc = set()
        self.answer = []
        self.dict = {}
        for i in range(len(nums) + 1):
            self.acc = set()
            self.answer.extend(self.backTracking(set(), i))

        self.temp = {str(x): 1 for x in self.answer}
        # self.answer = list(map(tuple, self.answer))
        # self.answer = list(set(self.answer))
        return self.temp.keys()

    def backTracking(self, curr, max_length):
        key = str(curr) + "|" + str(max_length)
        if key in self.memo:
            return []
        elif len(curr) == max_length:
            temp = sorted(list(curr))
            return [temp]


        answer = []
        for i in range(len(self.nums)):
            if self.nums[i] in curr:
                continue

            curr.add(self.nums[i])

            answer.extend(self.backTracking(curr, max_length))

            curr.remove(self.nums[i])

        self.memo[key] = answer
        return answer


nums = [1,2,3]
solution = Solution()
print(solution.subsets(nums))