from typing import *


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = dict(Counter(ransomNote))
        magazine_dict = dict(Counter(magazine))

        for key, value in ransomNote_dict.items():
            magazine_value = magazine_dict.get(key, 0)
            if value > magazine_value:
                return False

        return True