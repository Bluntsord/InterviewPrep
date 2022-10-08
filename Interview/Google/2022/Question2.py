from typing import *

def is_possible(a, b, c):
    d = a & b
    bin_d = bin(d)[2:]
    bin_c = bin(c)[2:]
    off_set = len(bin_c) - len(bin_d) if len(bin_c) > len(bin_d) else 0
    bin_c = bin_c[off_set:]
    for i in range(len(bin_d)):
        if bin_d == "1" and bin_c == "0":
            return False

    return True

print(is_possible(7, 19, 3))