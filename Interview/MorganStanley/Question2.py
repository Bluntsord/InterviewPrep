import bisect

n = 4
d = 10
k = 2
s = [2, 5, 4, 3]
e = [8, 9, 7, 5]
a = [800, 1600, 200, 400]
expected = 4500

meetings = []
answer = 0
from queue import PriorityQueue

def getMaxKnowledge(d, s, e, a, k):
    meetings = list(zip(s, e, a))
    meetings.sort(key=lambda x: x[0])
    check_points = s[:]
    check_points.extend(e)
    check_points = list(set(check_points))
    check_points.sort()
    answer = 0
    pq = PriorityQueue()
    for i in check_points:
        pq.queue.clear()
        curr_max = 0
        for meeting in meetings:
            if i >= meeting[0] and i <= meeting[1]:
                pq.put(-meeting[2])
        for j in range(k):
            if not pq.empty():
                curr_max -= pq.get()
        answer = max(answer, curr_max)
    return answer

print(getMaxKnowledge(d, s, e, a, k))