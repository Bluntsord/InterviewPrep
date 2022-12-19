from typing import *

def solution(a):
    a = [0] + a + [0]
    answer = []
    for i in range(1, len(a) - 1):
        curr = a[i - 1] + a[i] + a[i + 1]
        answer.append(curr)

    return answer

a = [4, 0, 1, -2, 3]
print(solution(a))

