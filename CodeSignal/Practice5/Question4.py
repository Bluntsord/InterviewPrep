def solution(a, k):
    start, stop = 0, max(a)

    while start < stop:
        mid = (start + stop) // 2
        curr = calculate_ribbons(a, mid)
        if curr == k:
            return curr
        if curr < k:
            start = mid + 1


def calculate_ribbons(ribbons, length):
    answer = [ribbon // length for ribbon in ribbons]
    return sum(answer)

