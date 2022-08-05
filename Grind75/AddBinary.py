class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_ptr, b_ptr, carry = len(a) - 1, len(b) - 1, 0
        answer = ""
        while a_ptr >= 0 or b_ptr >= 0:
            curr = int(a[a_ptr]) + int(b[b_ptr]) + carry
            if curr == 2:
                carry = 1
                curr = 0
            elif curr == 3:
                carry = 1
                curr = 1
            else:
                carry = 0
            answer += str(curr)
            a_ptr -= 1
            b_ptr -= 1
        return answer

a = "111"
b = "1"
solution = Solution()
print(solution.addBinary(a, b))
