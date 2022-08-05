class Solution:
    def combine(self, n: int, k: int):
        self.answer = []
        self.n = n
        self.k = k
        self.is_processed = False
        self.backTracking([], 1)
        return self.answer

    def backTracking(self, curr, lower_bound = 1):
        if len(curr) == self.k:
            temp = curr.copy()
            self.answer.append(temp)
            return

        for i in range(lower_bound, self.n + 1):
            curr.append(i)
            self.backTracking(curr, i + 1)
            curr.pop()

n = 6
k = 2
solution = Solution()
print(solution.combine(n, k))

