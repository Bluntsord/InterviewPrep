
#

def minimumCost(red, blue, blueCost):
    # Write your code here
    # Write your code here
    red_arr = [0]
    blue_arr = [0]

    for i in range(len(red)):
        red_cost = min(red_arr[-1], blue_arr[-1]) + red[i]
        blue_cost = min(red_arr[-1] + blueCost, blue_arr[-1]) + blue[i]
        red_arr.append(red_cost)
        blue_arr.append(blue_cost)
        
    temp = []
    for i in range(len(red)):
        res = min(red_arr[i], blue_arr[i])
        temp.append(res)

    return temp
