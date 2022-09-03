from typing import *


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_dict = {}
        for i in range(len(s)):
            curr = s[i]
            char_dict[curr] = i

        