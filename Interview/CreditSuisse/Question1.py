from collections import Counter

def areInputsBalancedAfterSwap(a: str, b:str):
    a_dict, b_dict = dict(Counter(a)), dict(Counter(b))
    a_set, b_set = [key for key in a_dict.keys()], [key for key in b_dict.keys()]
    a_len_set, b_len_set = create_len_dict(a_dict), create_len_dict(b_dict)
    if len(a_len_set) > 2 or len(b_len_set) > 2:
        return False

    for key_a in a_set:
        for key_b in b_set:
            handle_change(a_dict, b_dict, a_len_set, b_len_set, key_a, key_b)

            if len(a_len_set) == 1 or len(b_len_set) == 1:
                return True

            handle_change(a_dict, b_dict, a_len_set, b_len_set, key_b, key_a)

    return False

def handle_change(a_dict, b_dict, a_len_set, b_len_set, key_a, key_b):
    start_incr_a, end_incr_a = increment(a_dict, key_b)
    decrement(a_len_set, start_incr_a)
    increment(a_len_set, end_incr_a)

    start_decr_a, end_decr_a = decrement(a_dict, key_a)
    decrement(a_len_set, start_decr_a)
    increment(a_len_set, end_decr_a)

    start_incr_b, end_incr_b = increment(b_dict, key_a)
    decrement(b_len_set, start_incr_b)
    increment(b_len_set, end_incr_b)

    start_decr_b, end_decr_b = decrement(b_dict, key_b)
    decrement(b_len_set, start_decr_b)
    increment(b_len_set, end_decr_b)

def decrement(dictionary, key):
    if key is None:
        return

    start = dictionary.get(key, None)
    if dictionary[key] == 1:
        dictionary.pop(key)
    else:
        dictionary[key] -= 1
    return start, dictionary.get(key, None)

def increment(dictionary, key):
    if key is None:
        return
    start = dictionary.get(key, None)
    dictionary[key] = dictionary.get(key, 0) + 1

    return start, dictionary.get(key)

def create_len_dict(dictionary: dict):
    answer = {}
    for key, value in dictionary.items():
        answer[value] = answer.get(value, 0) + 1
    return answer


print(areInputsBalancedAfterSwap("kktt", "rree") == False)
print(areInputsBalancedAfterSwap("ddfg", "dccdfg") == True)
print(areInputsBalancedAfterSwap("dd", "dd") == True)
print(areInputsBalancedAfterSwap("ddfge", "zabc") == True)
print(areInputsBalancedAfterSwap("ddffeeee", "fabc") == True)
print(areInputsBalancedAfterSwap("dzffeeee", "fabc") == False)
