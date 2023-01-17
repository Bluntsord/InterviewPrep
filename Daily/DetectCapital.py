from typing import *

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower()):
            return True
        return False