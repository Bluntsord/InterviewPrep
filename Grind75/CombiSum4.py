from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.memo = {}
        self.candidates = candidates
        self.answer = []
        self.acc = []
        return self.answer

    def dp(self, pointer, target, curr) -> List[int]:
        key = str(curr)
        if target == 0:
            self.answer.append(curr.copy())
            return
        elif pointer >= len(self.candidates) or target < 0:
            return

        stay_list = curr.copy()
        stay_list.append(self.candidates[pointer])
        self.dp(pointer, target - self.candidates[pointer], stay_list)

        self.dp(pointer + 1, target, curr.copy())

        return

    def backTrackign(self, target):
        if target == 0:
            self.answer.append(self.acc.copy())
            return
        elif target < 0:
            return

        



candidates = [2, 3, 6, 7]
target3 = 7
nums = [1, 2, 3]
nums2 = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
target = 4
target2 = 10

solution = Solution()
print(solution.combinationSum(candidates, target3))
