def findPalindrome(s):
    return any(x==y for x,y in zip(s, s[1:])) or any(x==y for x,y in zip(s, s[2:]))

def nextLexicographicString(length, biggestAlphabet, string):
    # Convert string to list of ints
    string = [ord(x) - ord('a') for x in string]
    # Get the next string
    string = nextLexicographicStringHelper(length, biggestAlphabet, string)
    # Convert list of ints to string
    string = [chr(x + ord('a')) for x in string]
    return ''.join(string)

def nextLexicographicStringHelper(length, biggestAlphabet, string):
    # If the string is empty, return the first string
    if length == 0:
        return string
    recursed = False
    # If the last character is the biggest, then we need to increment the next character
    if string[length - 1] == biggestAlphabet - 1:
        string = nextLexicographicStringHelper(length - 1, biggestAlphabet, string)
        recursed = True
    # Increment the last character
    if recursed == False:
        string[length - 1] += 1
    else:
        string[length - 1] = 0
    if findPalindrome(string):
        return nextLexicographicStringHelper(length, biggestAlphabet, string)
    return string

print(nextLexicographicString(4, 5, 'eace'))