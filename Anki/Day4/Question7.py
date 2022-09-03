from typing import *


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            curr_char = s[i]
            if curr_char == "]":
                curr_word = ""
                while stack[-1] != "[":
                    curr_word = stack[-1] + curr_word
                    stack.pop()

                # Remove the open braces
                stack.pop()
                curr_number = ""

                while len(stack) != 0 and stack[-1].isdigit():
                    curr_number = stack[-1] + curr_number
                    stack.pop()
                curr_number = int(curr_number)
                word = curr_number * curr_word
                word_arr = [char for char in word]
                stack.extend(word_arr)
            if curr_char != "]":
                stack.append(curr_char)
        return "".join(stack)

s = "3[a]2[bc]"
solution = Solution()
print(solution.decodeString(s))
