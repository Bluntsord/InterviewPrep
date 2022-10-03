from typing import *

def teamSize(talent, talentCount):
    curr_window = {talent[0]: 1}
    left_pointer, right_pointer = 0, 1
    answer = []
    while right_pointer < len(talent):
        left_char = talent[left_pointer]
        while len(curr_window) < talentCount:
            right_char = talent[right_pointer]
            curr_window[right_char] = curr_window.get(right_char, 0) + 1
            right_pointer += 1
            if right_pointer >= len(talent):
                break
        curr_window_size = right_pointer - left_pointer
        answer.append(curr_window_size)

        if curr_window[left_char] == 1:
            curr_window.pop(left_char)
        else:
            curr_window[left_char] -= 1
        left_pointer += 1

    for i in range(left_pointer, len(talent)):
        left_char = talent[i]
        curr_val = len(talent) - i if len(curr_window) == talentCount else -1
        answer.append(curr_val)

        if curr_window[left_char] == 1:
            curr_window.pop(left_char)
        else:
            curr_window[left_char] -= 1
    return answer

talent = [2, 6, 1, 2, 3, 4, 2, 1, 5]
talentCount = 6
print(teamSize(talent, talentCount))
