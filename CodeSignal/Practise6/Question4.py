def solution(arr):
    if len(arr) <= 1:
        return 0
    left_pointer, right_pointer = 0, 1
    answer = 0
    prev_smaller = True if arr[left_pointer] < arr[right_pointer] else False

    while right_pointer < len(arr):
        if right_pointer == len(arr) - 1:
            if arr[right_pointer] != arr[right_pointer - 1]:
                answer += 1
            break

        while arr[right_pointer] != arr[right_pointer + 1] and prev_smaller != (arr[right_pointer] < arr[right_pointer + 1]):
            prev_smaller = arr[right_pointer] < arr[right_pointer + 1]
            right_pointer += 1
            if right_pointer == len(arr) - 1:
                break

        n = right_pointer - left_pointer + 1
        answer += (n - 1) * n / 2
        while right_pointer < len(arr) and arr[right_pointer] == arr[right_pointer - 1]:
            right_pointer += 1
        left_pointer = right_pointer - 1


    return int(answer)

arr = [10, 10, 10]
print(solution(arr))


