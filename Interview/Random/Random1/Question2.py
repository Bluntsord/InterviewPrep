from typing import *
from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        adj_list = {order[i]: order[i + 1] if i < len(order) - 1 else None for i in range(len(order))}

        root = None
        s_dict = dict(Counter(s))
        s_set = set(s)
        order_set = set(order)
        for letter in order:
            if letter in s_set:
                root = letter
                break

        for letter in order_set:
            if letter not in s_dict:
                s_dict[letter] = 0

        stack = [root]
        answer = ""

        while len(stack) != 0:
            curr_letter = stack.pop()
            answer += s_dict[curr_letter] * curr_letter
            neighbour = adj_list[curr_letter]

            if neighbour:
                stack.append(neighbour)

        for letter_not_in_order in s_set.difference(order_set):
            answer += s_dict[letter_not_in_order] * letter_not_in_order

        return answer

solution = Solution()
order = "cbafg"
s = "abcd"
print(solution.customSortString(order, s))







order = "cba"
s = "abcd"
solution = Solution()
print(solution.customSortString(order, s))
