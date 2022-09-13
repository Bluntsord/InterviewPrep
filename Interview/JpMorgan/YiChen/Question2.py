import sys

arr = []
for line in sys.stdin:
    arr.append(line)

def convert_digits(string):
    if string.isdigit():
        return int(string)
    return string

arr = list(map(lambda s: s.strip(), arr))
arr = list(map(convert_digits, arr))

print(arr)
