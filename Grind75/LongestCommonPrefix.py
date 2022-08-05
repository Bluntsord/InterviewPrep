class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ptr = 0
        answer = ""
        shortest = len(min(strs, key=len))
        while ptr < shortest:
            curr = strs[0][ptr]
            early_break = False
            for i in strs:
                if i[ptr] != curr:
                    early_break = True
                    break
            if not early_break:
                answer += curr
            else:
                break
            ptr += 1
        return answer

strs = ["flower","flow","flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs))




