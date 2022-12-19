def add_binary_strings(a, b):
    a = a[::-1]
    b = b[::-1]
    carry = 0
    result = ""
    for i in range(max(len(a), len(b))):
        if i < len(a):
            carry += int(a[i])
        if i < len(b):
            carry += int(b[i])
        result += str(carry % 2)
        carry //= 2
    if carry:
        result += str(carry)
    return result[::-1]

print(add_binary_strings("11", "1"))