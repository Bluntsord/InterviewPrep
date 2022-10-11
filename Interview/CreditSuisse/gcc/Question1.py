import math
from collections import defaultdict
def solution(n):
    for num in n:
        odd_factors, even_factors = get_divisors(num)
        if odd_factors > even_factors:
            print("SELL")
        elif odd_factors == even_factors:
            print("PASS")
        else:
            print("BUY")

def get_divisors(num: int):
    odd_factors, even_factors = 0, 0
    print(math.ceil(num ** 0.5))
    for i in range(2, math.ceil(num ** 0.5)):
        if num % i == 0:
            i_pair = num/i
            print(i, i_pair)
            if i % 2 == 1:
                odd_factors += 1
            else:
                even_factors += 1

            if i_pair % 2 == 1:
                odd_factors += 1
            else:
                even_factors += 1

    return odd_factors, even_factors


