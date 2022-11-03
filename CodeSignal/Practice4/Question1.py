def solution(numbers):
    return [is_zig_zag(numbers[i], numbers[i + 1], numbers[i + 2]) for i in range(len(numbers) - 2)]

def is_zig_zag(a, b, c):
    if a < b > c or a > b < c:
        return True
    return False