import math
from typing import *

def get_query_results(n: int, queries: List[List[int]]) -> List[int]:
    # Get good array
    good_arr = []
    temp = n
    while temp > 0:
        curr = math.floor(math.log2(temp))
        good_arr.append(2 ** curr)
        temp = temp - 2 ** curr
    good_arr.reverse()

    # Get prefix array
    prefix_arr = [1]
    curr = 1
    for i in range(len(good_arr)):
        curr = curr * good_arr[i]
        prefix_arr.append(curr)

    # Get answer
    answer = []
    for query in queries:
        curr = prefix_arr[query[1]]//(prefix_arr[query[0] - 1])
        curr = curr % query[2]
        answer.append(curr)

    return answer


n = 26
queries = [[1, 2, 1009], [3, 3, 5]]
print(get_query_results(n, queries))