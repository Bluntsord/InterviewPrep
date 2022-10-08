import math


def solution(numbers):
    max_power = math.ceil(math.log2(max(numbers) * 2))
    if min(numbers) < 0:
        min_power = 0
    else:
        min_power = math.floor(math.log2(min(numbers) * 2))

    numbers_set = {key: index for key, index in enumerate(numbers)}
    power_arr = [2 ** x for x in range(min_power, max_power + 1)]
    answer = 0
    for i in range(len(numbers)):
        for target in power_arr:
            if target - numbers[i] in numbers_set and numbers_set[target - numbers[i]] >= i:
                answer += 1

    return answer


numbers = [1, -1, 2, 3]
print(solution(numbers))




