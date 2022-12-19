def solution(a, b, k):
    if len(a) == 0:
        return 0

    answer = 0
    for i in range(len(a)):
        curr = int(str(a[i]) + str(b[-i]))
        if curr < k:
            answer += 1

    return answer

a = [1, 2, 3]
b = [1, 2, 3]
k = 31
print(solution(a, b, k))
