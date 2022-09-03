def solution(s1, s2):
    s1_dict = {}
    s2_dict = {}
    for i in range(len(s1)):
        s1_dict[s1[i]] = s1_dict.get(s1[i], 0) + 1
    for i in range(len(s2)):
        s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1
    answer = helper(s1, s2, s1_dict, s2_dict)
    return answer



def helper(first_string, second_string, s1_dict, s2_dict):
    if len(first_string) == 0 and len(second_string) == 0:
        return ""
    elif len(first_string) == 0:
        return second_string
    elif len(second_string) == 0:
        return first_string

    s1_number = s1_dict[first_string[0]]
    s2_number = s2_dict[second_string[0]]
    if s1_number == s2_number:
        if first_string[0] <= second_string[0]:
            return first_string[0] + helper(first_string[1:], second_string, s1_dict, s2_dict)
        else:
            return second_string[0] + helper(first_string, second_string[1:], s1_dict, s2_dict)
    elif s1_number < s2_number:
        return first_string[0] + helper(first_string[1:], second_string, s1_dict, s2_dict)
    return second_string[0] + helper(first_string, second_string[1:], s1_dict, s2_dict)






