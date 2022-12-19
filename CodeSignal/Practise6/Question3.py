from collections import Counter

def solution(s1, s2):
    first_pointer, second_pointer = 0, 0
    first_char_dict, second_char_dict = dict(Counter(s1)), dict(Counter(s2))
    def compare(first_letter, second_letter):
        first_occurrence, second_occurrence = first_char_dict.get(first_letter, 0), second_char_dict.get(second_letter, 0)
        if first_occurrence == second_occurrence:
            if first_letter == second_letter:
                return True
            return first_letter < second_letter
        elif first_occurrence < second_occurrence:
            return True
        return False

    answer = ""
    while first_pointer < len(s1) and second_pointer < len(s2):
        first_letter, second_letter = s1[first_pointer], s2[second_pointer]
        if compare(first_letter, second_letter):
            answer += first_letter
            first_pointer += 1
        else:
            answer += second_letter
            second_pointer += 1

    if first_pointer == len(s1):
        answer += s2[second_pointer:]
    elif second_pointer == len(s2):
        answer += s1[first_pointer:]

    return answer

first = "ougtaleegvrabhugzyx"
second = "wvieaqgaegbxg"
print(solution(first, second))


