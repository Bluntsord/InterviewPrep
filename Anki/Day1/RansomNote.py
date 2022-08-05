from typing import *


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = Counter(ransomNote)
        magazine_dict = Counter(magazine)

        for letter in ransom_dict.keys():
            if letter not in magazine_dict or ransom_dict[letter] > magazine_dict[letter]:
                return False


        return True

ransom_note = "aa"
mag = "aab"
solution = Solution()
print(solution.canConstruct(ransom_note, mag))