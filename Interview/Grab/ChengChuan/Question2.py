def solution(s):
    s = [char for char in s]
    for i in range(len(s)):
        if i >= len(s) // 2:
            break
        curr = s[i]
        back = s[len(s) - 1 - i]

        if (curr == "?" or back == "?"):
            if curr == "?" and back == "?":
                s[i] = "z"
                s[len(s) - 1 - i] = "z"
            elif curr == "?":
                s[i] = back
            else:
                s[len(s) - 1 - i] = curr
        else:
            return "NO"

    return "".join(s)


temp = solution("?a?")
print(temp)