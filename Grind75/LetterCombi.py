from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.letter_dict = {
            2: ("a", "b", "c"),
            3: ("d", "e", "f"),
            4: ("g", "h", "i"),
            5: ("j", "k", "l"),
            6: ("m", "n", "o"),
            7: ("p", "q", "r", "s"),
            8: ("t", "u", "v"),
            9: ("w", "x", "y", "z")
        }

        self.answer = []
        temp = self.dp(digits)
        return temp

    def dp(self, curr_string):
        if len(curr_string) == 0:
            return []
        elif len(curr_string) == 1:
            answer = self.letter_dict[int(curr_string[0])]
            answer = list(answer)
            return answer

        first_number = curr_string[0]
        remaining_number = curr_string[1:]
        mapped_letters = self.letter_dict[int(first_number)]
        wish = self.dp(remaining_number)
        answer = {}

        for i in mapped_letters:
            for j in wish:
                curr = i + j
                answer[curr] = 1

        answer = list(answer.keys())
        return answer

digits = ""
solution = Solution()
print(solution.letterCombinations(digits))









