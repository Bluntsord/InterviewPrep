def solution(a):
    length = len(a)
    a.insert(0, 0)
    a.append(0)
    acc = a[0] + a[1]
    answer = [acc]
    for i in range(2, 1 + length):
        acc += a[i + 1]
        acc -= a[i - 2]
        answer.append(acc)
    return answer


