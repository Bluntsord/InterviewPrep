class Solution:
    def subsets(self, nums):
        self.nums = nums
        self.answer = []
        self.visited = {}
        self.dict = {}
        self.backTracking([], 0)
        self.answer.sort(key=len)
        return self.answer

    def backTracking(self, curr, lower_bound):
        curr.sort()
        key = "|".join(list(map(str, curr)))
        if key in self.visited:
            return
        self.visited[key] = 1
        self.answer.append(curr[:])
        if len(curr) == len(self.nums):
            return

        for i in range(lower_bound, len(self.nums)):
            num = self.nums[i]
            if len(curr) != 0 and curr[0] == 0:
                print('here')
            if num in self.dict:
                continue
            curr.append(num)
            self.dict[num] = 1
            self.backTracking(curr, i + 1)
            self.dict.pop(num)
            curr.pop()

nums = [4, 1, 0]
solution = Solution()
print(solution.subsets(nums))
