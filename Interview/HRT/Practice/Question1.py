def solution(numbers):
    return [is_zig_zag(numbers, i) for i in range(len(numbers) - 2)]

def is_zig_zag(numbers, pointer):
    first, second, third = numbers[pointer], numbers[pointer + 1], numbers[pointer + 2]
    if first < second > third or first > second < third:
        return 1
    return 0

numbers = [1, 2, 1, 3, 4]
print(solution(numbers))