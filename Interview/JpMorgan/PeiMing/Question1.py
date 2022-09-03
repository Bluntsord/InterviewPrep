from collections import Counter

def areAlmostEquivalent(first_arr, second_arr):
    return [is_almost_equivalent(first_arr[i], second_arr[i]) for i in range(len(first_arr))]

def is_almost_equivalent(first_word, second_word):
    if len(first_word) != len(second_word):
        return "NO"
    first_dict = dict(Counter(first_word))
    second_dict = dict(Counter(second_word))

    for key, value in first_dict.items():
        second_dict_value = second_dict.get(key, 0) + 1
        if value - second_dict_value > 3:
            return "NO"

    for key, value in second_dict.items():
        first_dict_value = first_dict.get(key, 0) + 1
        if value - first_dict_value > 3:
            return "NO"

    return "YES"


s = ["aabaab", "aaaaabb"]
t = ["bbabbc", "aab"]
print(areAlmostEquivalent(s, t))

