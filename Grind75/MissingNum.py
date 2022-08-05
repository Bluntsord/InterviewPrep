class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        supposed_sum = (n / 2) * (2 + (n - 1))
        curr = sum(nums)
        return int(supposed_sum - curr)

n = [3, 0, 1]
solution = Solution()
print(solution.missingNumber(n))
