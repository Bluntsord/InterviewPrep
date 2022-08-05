import queue

class Solution(object):
    def __init__(self):
        self.queue = queue.Queue()
        self.sum = 2

    def tribonacci(self, n):
        self.queue = queue.Queue()
        list(map(self.queue.put, [0, 1, 1]))
        self.sum = 2
        return self.dp(n)

    def dp(self, n):
        if n < 0:
            return -1
        elif n < 3:
            return list(self.queue.queue)[n]

        for i in range(n - 2):
            first, last = self.queue.get(), self.sum
            self.queue.put(last)
            self.sum = self.sum * 2 - first

        return list(self.queue.queue)[2]

solution = Solution()
print(solution.tribonacci(5))
