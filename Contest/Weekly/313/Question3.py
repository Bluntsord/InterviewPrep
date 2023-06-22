from typing import *


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        number_of_bits = bin(num2).count("1")
        num1_in_bits = bin(num1)

        num1_in_bits = num1_in_bits[2:]

        if len(num1_in_bits) < number_of_bits:
            prepend = (number_of_bits - len(num1_in_bits) + 1) * "0"
            num1_in_bits = prepend + num1_in_bits
        answer = []
        for i in range(len(num1_in_bits)):
            curr_num1_bit = num1_in_bits[i]
            if curr_num1_bit == "1" and number_of_bits > 0:
                answer.append(1)
            else:
                answer.append(0)
            number_of_bits -= 1 if curr_num1_bit == "1" else 0

        temp, acc = 0, 0
        for i in reversed(range(len(answer))):
            if answer[i] != 1 and number_of_bits > 0:
                answer[i] = 1
                number_of_bits -= 1

            if answer[i] == 1:
                temp += 2 ** acc

            acc += 1

        return temp



solution = Solution()
print(solution.minimizeXor(3, 5))
