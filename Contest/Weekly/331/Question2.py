from typing import *


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        vowel_array = [1 if word[0] in vowel and word[-1] in vowel else 0 for word in words]

        prefix_sum = []
        acc = 0
        for vowel in vowel_array:
            acc += vowel
            prefix_sum.append(acc)


        def get_query(query):
            if query[0] <= 0:
                return prefix_sum[query[1]]
            elif query[1] >= len(prefix_sum):
                return prefix_sum[-1]

            return prefix_sum[query[1]] - prefix_sum[query[0] - 1]

        return [get_query(query) for query in queries]
