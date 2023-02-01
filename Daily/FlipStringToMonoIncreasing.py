from typing import *


class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        prefix, prefix_ones = 0, []
        for i in range(len(s)):
            prefix += 1 if s[i] == "1" else 0
            prefix_ones.append(prefix)

        suffix, suffix_zeros = 0, []
        for i in reversed(range(len(s))):
            suffix += 1 if s[i] == "0" else 0
            suffix_zeros.append(suffix)



