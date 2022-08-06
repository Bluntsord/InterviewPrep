from typing import *

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        name_stack = self.helper(name)
        typed_stack = self.helper(typed)
        print(name_stack)
        print(typed_stack)
        if len(name_stack) != len(typed_stack):
            return False

        for i in range(len(name_stack)):
            if name_stack[i][1] > typed_stack[i][1] or name_stack[i][0] != typed_stack[i][0]:
                return False
        return True


    def helper(self, word):
        stack = [[word[0], 1]]
        for i in range(len(word)):
            prev_letter = stack[len(stack) - 1][0]
            if word[i] == prev_letter:
                stack[len(stack) - 1][1] += 1
            else:
                curr = [word[i], 1]
                stack.append(curr)
        return stack


name = "a"
typed = "b"


solution = Solution()
print(solution.isLongPressedName(name, typed))