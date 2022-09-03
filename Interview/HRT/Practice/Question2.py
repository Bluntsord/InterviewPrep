def solution(a):
    left_pointer, right_pointer = 0, len(a) - 1
    answer = []
    while left_pointer < right_pointer:
        answer.append(a[left_pointer])
        answer.append(a[right_pointer])
        left_pointer += 1
        right_pointer -= 1

    if left_pointer == right_pointer:
        answer.append(a[right_pointer])

    for i in range(1, len(answer)):
        if answer[i - 1] >= answer[i]:
            return False
    return True
