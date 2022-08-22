import math
from typing import *

def solution(numbers, left, right):
    answer = []
    for i in range(len(numbers)):
        curr = numbers[i]
        temp = curr/(i + 1)
        if left <= temp <= right and math.floor(temp) == temp:
            answer.append(True)
        else:
            answer.append(False)
    return answer


nums = [8,5, 6,16, 5]
left = 1
right = 3
answer = [False, False, True, False, True]

print(solution(nums, left, right))