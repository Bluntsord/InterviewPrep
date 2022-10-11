from collections import Counter

def solution(files):
    # Write solution here
    word_dict = dict(Counter(files))
    answer, odd = 0, 0
    for key, value in word_dict.items():
        if value % 2 == 1:
            odd = 1
            answer += value - 1
        else:
            answer += value

    answer += odd
    return answer


def main():
    str = input()
    answer = solution(str)
    print(answer)
