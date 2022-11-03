def solution(a):
    char_dict = {}
    for number in a:
        number_str = str(number)
        for char in number_str:
            char_dict[char] = char_dict.get(char, 0) + 1

    max_value = max(char_dict.values())
    answer = [key for key, value in char_dict if value == max_value]

    return answer

