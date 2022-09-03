import time
from collections import deque

class Solution:
    def __init__(self):
        self.memo = {}
        self.steps = 0
        self.badIndex = 0

    def maximise(self, steps, badIndex):
        self.memo = {}
        self.steps = steps
        self.badIndex = badIndex
        answer = self.dp(0, 1)

        return answer

    def dp(self, pointer, j):
        key = str(pointer) + "|" + str(j)
        if j == self.steps + 1:
            return pointer
        elif pointer == self.badIndex:
            return 0
        elif key in self.memo:
            return self.memo[key]

        take_curr = self.dp(pointer + j, j + 1)
        drop_curr = self.dp(pointer, j + 1)
        answer = max(take_curr, drop_curr)
        self.memo[key] = answer

        return answer

    def temp(self, steps, badIndex):
        pointer, j = 0, 1
        hit_bad_index = False
        for i in range(steps):
            if pointer == badIndex:
                hit_bad_index = True
            pointer += j
            j += 1

        return pointer if not hit_bad_index else pointer - 1




solution = Solution()
a = 37
b = 24

start_time = time.time()
print(solution.maximise(a, b))

end_time = time.time()
print(end_time - start_time)
print("-====")

start_time = time.time()
print(solution.temp(a, b))

end_time = time.time()
print(end_time - start_time)
print("-====")




