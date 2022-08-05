from typing import *


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decode_dict = {}
        curr = 'a'
        key = key.replace(" ", "")
        alphabets = ""
        i = 0
        while curr != '{':
            if key[i] in decode_dict:
                i += 1
                continue
            elif i == 25:
                print("here")
            alphabets += curr
            decode_dict[key[i]] = curr
            curr = chr(ord(curr) + 1)
            i += 1

        decode_dict[" "] = " "
        print(decode_dict["l"])


        acc = ""
        for character in message:
            new_char = decode_dict[character]
            acc += new_char

        return acc

key = "fjvnpgmknxzcdpasmterbhsihyqbzakgahwwcolatuopdlcjyfossvei"
message = "dt debylrqlocf"

#key = "the quick brown fox jumps over the lazy dog"
#message = "vkbs bs t suepuv"
solution = Solution()
print(solution.decodeMessage(key, message))
