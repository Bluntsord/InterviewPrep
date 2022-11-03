import bisect


def solution(a, k):
    mod_arr = [num % k for num in a]
    mod_index_dict = {}
    for index, mod in enumerate(mod_arr):
        if mod not in mod_index_dict:
            mod_index_dict[mod] = [index]
        else:
             mod_index_dict[mod].append(index)

    answer = 0
    for mod, indexes in mod_index_dict.items():
        if mod == 0:
            continue
        if k - mod not in mod_index_dict:
            continue
        elif k - mod == mod:
            answer += same_arr(indexes)
        else:
            pair_indexes = mod_index_dict[k - mod]
            answer += helper(indexes, pair_indexes)

    if 0 not in mod_index_dict:
        return answer

    return answer + same_arr(mod_index_dict[0])

def helper(first_arr, second_arr):
    answer = 0
    for num in first_arr:
        insert_index = bisect.bisect_left(second_arr, num)
        answer += len(second_arr) - insert_index

    return answer

def same_arr(first_arr):
    mod_0_len = len(first_arr)
    temp = ((mod_0_len - 1)/2) * (2 + (mod_0_len - 2))
    return int(temp)



