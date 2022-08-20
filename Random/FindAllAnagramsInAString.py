from typing import *


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s = s + "!"
        char_dict = dict(Counter(p))
        curr_dict = dict(Counter(s[:len(p)]))
        left_pointer, right_pointer = 0, len(p) - 1
        answer = []

        while right_pointer < len(s) - 1:
            if curr_dict == char_dict:
                answer.append(left_pointer)

            left_pointer += 1
            right_pointer += 1
            right_letter = s[right_pointer]
            left_letter = s[left_pointer - 1]

            curr_dict[right_letter] = curr_dict.get(right_letter, 0) + 1
            if curr_dict[left_letter] == 1:
                curr_dict.pop(left_letter)
            else:
                curr_dict[left_letter] -= 1


        return answer



s = "abab"
p = "abab"

solution = Solution()
print(solution.findAnagrams(s, p))
