class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        answer = 0
        for i in range(len(s) - 1):
            curr = s[i]
            next = s[i + 1]
            if mapping[curr] >= mapping[next]:
                answer += mapping[curr]
            else:
                answer -= mapping[curr]
        answer += mapping[s[len(s) - 1]]
        return answer

a = "MCMXCIV"
solution = Solution()
print(solution.romanToInt(a))
