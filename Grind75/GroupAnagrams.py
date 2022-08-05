from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for word in strs:
            sorted_word = sorted(word)
            sorted_word = ''.join(sorted_word)
            if sorted_word not in word_dict:
                word_dict[sorted_word] = []
            curr = word_dict[sorted_word]
            curr.append(word)

        answer = []
        for items in word_dict.values():
            answer.append(items)
        return answer

strs = ["eat","tea","tan","ate","nat","bat"]

solution = Solution()
print(solution.groupAnagrams(strs))
