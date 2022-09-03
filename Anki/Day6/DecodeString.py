class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            curr = s[i]
            if curr == "]":
                word = ""
                while stack[-1] != "[":
                    word = stack.pop() + word
                stack.pop()
                number = ""
                while stack[-1].isdigit():
                    number = stack.pop() + number
                number = int(number)
                final_word = number * word
                for char in final_word:
                    stack.append(char)
        return stack



