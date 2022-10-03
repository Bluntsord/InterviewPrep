from typing import *
from queue import PriorityQueue

def smashTheBricks(bigHits, newtons):
    pq = PriorityQueue()
    for index, newtons in enumerate(newtons):
        pq.put(-newtons, index)

    bigHits_arr, smallHits_arr = [], []
    bigHitSet = set()
    while bigHits > 0:
        newtons, index = pq.get()
        newtons = - newtons
        bigHits_arr.append(index)
        bigHitSet.add(index)

    for i in range(len(newtons)):
        if i in bigHitSet:
            continue
        smallHits_arr.append(i)

    return []




newtons = [2, 3, 1]
bigHits = 1
smashTheBricks(bigHits, newtons)