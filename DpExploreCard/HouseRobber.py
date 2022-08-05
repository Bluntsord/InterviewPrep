class Solution(object):
    def __init__(self):
        self.memo = {}
        self.nums = None

    def rob(self, nums):
        self.memo = {}
        self.nums = nums
        return self.dp(0)

    def dp(self, pointer):
        if pointer >= len(self.nums):
            return 0
        elif pointer in self.memo:
            return self.memo[pointer]

        curr = self.nums[pointer]
        steal_here = self.dp(pointer + 2) + curr
        move_next = self.dp(pointer + 1)

        answer = max(steal_here, move_next)
        self.memo[pointer] = answer

        return answer

solution = Solution()
nums = [1,5,3,1]
nums2 = [2,7,9,3,1]
print(solution.rob(nums2))

