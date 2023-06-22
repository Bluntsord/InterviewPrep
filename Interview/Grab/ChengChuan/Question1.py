from typing import *
from collections import Counter

def solution(s):
    s_counter = Counter(s)
    for key, value in s_counter.items():
        if value == 2:
            return key

    return 0

print(solution("aab"))

