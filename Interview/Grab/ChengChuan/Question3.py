def sum_digits(s):
    s_char = [char for char in str(s)]
    answer = 0
    for char in s_char:
        answer += int(char)

    return answer

def solution(A):
    a_sum = list(map(lambda x: sum_digits(x), A))
    a_dict = {key: [] for key in a_sum}

    for i in range(len(A)):
        curr_sum = a_sum[i]
        curr_stack = a_dict[curr_sum]

        if len(curr_stack) == 2:
            curr_stack.append(A[i])
            curr_stack.sort()
            a_dict[curr_sum] = curr_stack[1:]
        else:
            curr_stack.append(A[i])

    answer = -1
    for key, values in a_dict.items():
        if len(values) < 2:
            continue
        curr_max = sum(values)
        answer = max(curr_max, answer)

    return answer

print(solution([51, 71, 17, 42]))
print(solution([42, 33, 60]))
print(solution([51, 32, 43]))





