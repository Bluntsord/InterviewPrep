import bisect

a = [i for i in range(1, 10, 2)]
print(a)
coord = bisect.bisect_left(a, 3)
coord = bisect.bisect_right(a, 3)
another_coord = bisect.bisect_left(a, 4)
another_coord = bisect.bisect_right(a, 4)
print(coord)
print(another_coord)
