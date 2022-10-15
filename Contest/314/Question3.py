class Solution:
    def robotWithString(self, s: str) -> str:
        if len(s) == 0:
            return ""

        front = s[-1] + s[1:]
        back = s[1:] + s[-1]
        return front if front < back else back


solution = Solution()
print(solution.robotWithString("zza"))
