class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        first_stack, second_stack = [], []

        for i in s:
            if i == "#" and len(first_stack) != 0:
                first_stack.pop()
            elif i == "#":
                continue
            else:
                first_stack.append([i])

        for j in t:
            if j == "#" and len(second_stack) != 0:
                second_stack.pop()
            elif j == "#":
                continue
            else:
                second_stack.append([j])
        if len(first_stack) != len(second_stack):
            return False
        for i in range(len(first_stack)):
            if second_stack[i] != first_stack[i]:
                return False

        return True
a = "isfcow#"
b = "isfco#w#"
solution = Solution()
print(solution.backspaceCompare(a, b))


