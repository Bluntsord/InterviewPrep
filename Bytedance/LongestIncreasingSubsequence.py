nums = [10,9,2,5,3,7,101,18]
nums2 = [2,15,3,7,8,6,18]
print(len(nums2))

class Solution(object):
    memo = {}
    def lengthOfLIS(self, nums):
        self.memo = {}
        answer = []
        return len(self.dp(0, nums, float('-inf'), answer))

    def dp(self, pointer, nums, previous_num, answer):
        if pointer >= len(nums):
            return answer
        curr = nums[pointer]
        if curr > previous_num:
            temp = answer.copy()
            temp.append(curr)
            take_current = self.dp(pointer + 1, nums, curr, temp)
            drop_current = self.dp(pointer + 1, nums, previous_num, answer)
            temp = drop_current if len(drop_current) > len(take_current) else take_current
            return temp
        elif pointer in self.memo:
            return self.memo[pointer]

        drop_current = self.dp(pointer + 1, nums, previous_num, answer)
        restart = self.dp(pointer + 1, nums, curr, [curr])
        temp = drop_current if len(drop_current) > len(restart) else restart
        return temp

solution = Solution()
print(solution.lengthOfLIS(nums2))