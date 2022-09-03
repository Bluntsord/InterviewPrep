from typing import *


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        number_of_0 = 0
        number_of_1 = 0
        for i in range(1, len(boxes)):
            if boxes[i] == "1":
                number_of_1 += 1

        total_moves = 0
        for i in range(1, len(boxes)):
            if boxes[i] == "1":
                total_moves += i

        number_of_1_on_left = 0
        number_of_1_on_right = number_of_1
        # print(number_of_1_on_right)
        answer = [total_moves]
        for i in range(1, len(boxes)):
            if boxes[i] == "1":
                number_of_1_on_right -= 1
            if boxes[i - 1] == "1":
                number_of_1_on_left += 1
            print("-----")
            print(number_of_1_on_left)
            print(number_of_1_on_right)
            total_moves += number_of_1_on_left
            total_moves -= number_of_1_on_right
            answer.append(total_moves)

        return answer

boxes = "110"
boxes = "001011"
solution = Solution()
print(solution.minOperations(boxes))

