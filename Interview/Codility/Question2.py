non_vowel = ["a", "e", "i", "o", "u"]
non_vowel = set(non_vowel)

def check_curr(first_string, pattern):
    answer = True
    for i in range(len(pattern)):
        if pattern[i] == "0":
            temp = first_string[i] in non_vowel
            answer = answer and temp
        else:
            temp = first_string[i] not in non_vowel
            answer = answer and temp
    return answer

def solution(pattern, source):
    start = source[:len(pattern)]
    answer = 0
    for i in range(len(pattern), len(source)):
        print(start)
        if check_curr(start, pattern):
            # print('=')
            answer += 1

        start = start[1:] + source[i]
    if check_curr(start, pattern):
        answer += 1
    return answer


