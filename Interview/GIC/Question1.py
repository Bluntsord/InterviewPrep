def solution(word, roll):
    postfix = [0 for _ in range(len(word))]
    for curr_roll in roll:
        postfix[curr_roll - 1] += 1

    for i in reversed(range(len(word) - 1)):
        postfix[i] += postfix[i + 1]

    letter_map = [char for char in word]
    answer = [roll_letter(letter_map[i], postfix[i]) for i in range(len(word))]

    answer = ''.join(answer)

    return answer

def roll_letter(letter, number):
    if 'a' <= letter <= 'z':
        base = ord('a')
    elif 'A' <= letter <= 'Z':
        base = ord('A')
    else:
        raise ValueError("Invalid input. Please input an alphabet character.")

    offset = ord(letter) - base
    new_offset = (offset + number) % 26
    rolled_letter = chr(new_offset + base)

    return rolled_letter



print(solution("abz", [2, 2, 1]))
