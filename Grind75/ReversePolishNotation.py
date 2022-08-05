class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            print(stack)
            if token in operators:
                second = int(stack.pop())
                first = int(stack.pop())
                if token == "+":
                    temp = first + second
                elif token == "-":
                    temp = first - second
                elif token == "*":
                    temp = first * second
                elif token == "/":
                    temp = first / second
                stack.append(temp)
            else:
                stack.append(token)
        answer = stack.pop()
        return answer
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
solution = Solution()
print(solution.evalRPN(tokens))