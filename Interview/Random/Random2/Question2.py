import numpy as np

def add_one(number):
    for i in range(5):
        print(i)
        yield i + 1

temp = add_one(1)
print(next(temp))
print(next(temp))
print()
