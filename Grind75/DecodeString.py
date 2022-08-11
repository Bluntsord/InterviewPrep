from typing import *


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            curr = s[i]
            if curr == "]":
                top_of_stack = stack.pop()
                curr_string = top_of_stack
                while stack[-1] != "[":
                    top_of_stack = stack.pop()
                    curr_string = top_of_stack + curr_string
                open_bracket = stack.pop()
                multiple = ""
                while len(stack) != 0 and stack[-1].isnumeric():
                    temp = stack.pop()
                    multiple = temp + multiple
                multiple = int(multiple)
                curr_string = multiple * (curr_string)
                for char in curr_string:
                    stack.append(char)
            else:
                stack.append(curr)
        answer = ''.join(stack)
        return answer

s = "3[a]2[bc]"
s = "3[a2[c]]"
s = "100[leetcode]"
solution = Solution()
print(solution.decodeString(s))