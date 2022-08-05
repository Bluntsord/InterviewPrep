class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = list(map(lambda x: x ** 2, nums))
        temp.sort()
        return temp

nums = [0, 1, 2]
solution = Solution()
print(solution.sortedSquares(nums))