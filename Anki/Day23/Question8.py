class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = "0b" + a
        b = "0b" + b
        answer = int(b, 2) + int(a, 2)
        print(answer)

solution = Solution()
print(solution.addBinary("11", "1"))