class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""

        for i in range(len(s)):
            # Odd length
            left_ptr, right_ptr = i, i
            while left_ptr >= 0 and right_ptr < len(s) and s[left_ptr] == s[right_ptr]:
                if right_ptr - left_ptr + 1 > len(res):
                    res = s[left_ptr: right_ptr + 1]
                left_ptr -= 1
                right_ptr += 1

            # Even length
            left_ptr, right_ptr = i, i + 1
            while left_ptr >= 0 and right_ptr < len(s) and s[left_ptr] == s[right_ptr]:
                if right_ptr - left_ptr + 1 > len(res):
                    res = s[left_ptr:right_ptr + 1]
                left_ptr -= 1
                right_ptr += 1
        return res

solution = Solution()
print(solution.longestPalindrome("cbbd"))

