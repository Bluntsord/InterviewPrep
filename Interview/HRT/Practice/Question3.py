def solution(a):
    number_dict = {}
    answer = []
    for i in range(len(a)):
        curr_arr = a[i]
        curr_avg = get_mean(curr_arr)
        temp = number_dict.get(curr_avg, [])
        temp.append(i)
        number_dict[curr_avg] = temp

    curr_temp = list(number_dict.values())

    curr_temp.sort(key=lambda x:x[0])
    return curr_temp



def get_mean(nums):
    return sum(nums)/len(nums)

curr = [[1,2], [3, 4]]
print(solution(curr))