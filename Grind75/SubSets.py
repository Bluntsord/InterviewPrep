from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.visited = {}
        self.answer = []
        self.backTracking(nums)

        return self.answer

    def backTracking(self, curr):
        curr_copy = curr.copy()
        curr_copy.sort()
        key = "|".join(list(map(str, curr_copy)))
        if len(curr_copy) == 0:
            return

        if key not in self.visited:
            self.answer.append(curr_copy.copy())
            self.visited[key] = 1

        for char in curr_copy:
            curr_copy.remove(char)
            self.backTracking(curr_copy)
            curr_copy.append(char)

        return

nums = [1,2,3]
solution = Solution()
print(solution.subsets(nums))










nums = [1,2,3]
solution = Solution()
print(solution.subsets(nums))





