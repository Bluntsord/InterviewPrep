def solution(s, t):
    answer = 0
    for i in range(len(s)):
        curr = s[i]
        if curr.isdigit():
            answer += 1 if s[:i] + s[i + 1:] < t else 0

    for i in range(len(t)):
        curr = t[i]
        if curr.isdigit():
            answer += 1 if t[:i] + t[i + 1:] > s else 0

    return answer

