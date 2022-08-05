from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        self.nums = nums
        self.visited = {}
        self.backTracking([])
        return self.answer

    def backTracking(self, stack):
        if len(stack) == len(self.nums):
            self.answer.append(stack.copy())
            return

        for num in nums:
            if num not in self.visited:
                stack.append(num)
                self.visited[num] = 1
                self.backTracking(stack)
                stack.pop()
                self.visited.pop(num)



solution = Solution()
nums = [1,2,3]
print(solution.permute(nums))