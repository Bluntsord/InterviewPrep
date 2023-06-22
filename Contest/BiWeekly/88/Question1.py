from collections import Counter
from collections import defaultdict

class Solution:
    def equalFrequency(self, word: str) -> bool:
        self.letter_dict = dict(Counter(word))
        frequency_dict = {}
        for letter, frequency in self.letter_dict.items():
            frequency_dict[frequency] = frequency_dict.get(frequency, 0) + 1
        print(frequency_dict)
        return self.check_all_same(frequency_dict)

    def check_all_same(self, frequency_dict: dict):
        if len(frequency_dict) > 2:
            return False
        elif len(frequency_dict) == 2:
            frequency_arr = list(frequency_dict.keys())
            frequency_arr.sort()
            if frequency_arr[1] - frequency_arr[0] == 1 and frequency_dict[frequency_arr[1]] == 1:
                return True
            elif frequency_arr[0] == 1 and frequency_dict[frequency_arr[0]] == 1:
                return True
            return False
        elif len(frequency_dict) == 1:
            frequency_arr = list(frequency_dict.keys())
            return frequency_arr[0] == 1 or len(self.letter_dict) == 1
        return False

word = "zz"
solution = Solution()
print(solution.equalFrequency(word))