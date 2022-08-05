from collections import Counter


class Solution(object):
    def deleteAndEarn(self, nums):
        count = Counter(nums)
        nums = sorted(list(set(nums)))

        earn1, earn2 = 0, 0

        for i in range(len(nums)):
            curr = nums[i]
            currEarn = curr * count[curr]

            temp = earn2
            if i > 0 and nums[i - 1] + 1 == curr:
                earn2 = max(earn2, earn1 + currEarn)
            else:
                earn2 += currEarn
            earn1 = temp

        return earn2

nums = [3, 4, 2]
solution = Solution()
print(solution.deleteAndEarn(nums))



            





