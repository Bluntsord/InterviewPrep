import math
from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp_dict = Counter(s)
        ans = 0
        oneIncluded = 0
        for key in temp_dict:
            curr = temp_dict[key]
            if curr % 2 == 1 and oneIncluded == 0:
                ans += 1
                oneIncluded = 1
            elif curr == 1:
                continue
            temp_add = curr if curr % 2 == 0 else curr - 1
            ans += temp_add
        return ans


s = "abccccdd"
solution = Solution()
print(solution.longestPalindrome(s))
