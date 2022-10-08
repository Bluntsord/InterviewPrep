import math

def isPossible(a, b, c, d):
    memo = {}

    def dp(a, b, startA, startB):
        if a > c or b > d:
            return False
        elif a == c:
            return (d - b) % a == 0
        elif b == d:
            return (c - a) %  b == 0
        elif (a, b) in memo:
            return memo[(a, b)]

        take_first = dp(a + b, b)
        if take_first:
            memo[(a, b)] = take_first
            return take_first

        take_second = dp(a, a + b)
        answer = take_second
        memo[(a, b)] = answer

        return answer

    return "Yes" if dp(a, b, 1, 1) else "No"




