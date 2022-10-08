from typing import *

def transformArray(arrayA, arrayB):
    if len(arrayA) == 0 and len(arrayB) == 0:
        return True
    arrayA = [int(a) for a in arrayA]
    arrayB = [int(b) for b in arrayB]
    arrayA_dict = dict(Counter(arrayA))
    arrayB_dict = dict(Counter(arrayB))
    for i in range(len(arrayA)):
        temp = arrayA_dict.copy()
        for j in range(i + 1):
            if temp[arrayA[j]] == 1:
                temp.pop(arrayA[j])
            else:
                temp[arrayA[j]] -= 1

            curr = arrayA[j] + 1
            temp[curr] = temp.get(curr, 0) + 1
            if arrayB_dict == temp:
                return True

    return False


arrayA = "135"
arrayB = "245"
print(transformArray(arrayA, arrayB))