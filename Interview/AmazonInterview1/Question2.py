from typing import *

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes = list(map(lambda x: (x[0], x[1]), dominoes))
        domino_dict = {}
        for domino in dominoes:
            inverted = (domino[1], domino[0])
            if domino not in domino_dict and inverted not in domino_dict:
                domino_dict[domino] = 1
            else:
                if domino in domino_dict:
                    domino_dict[domino] += 1
                else:
                    domino_dict[inverted] += 1

        answer = 0
        for items in domino_dict.items():
            if items[1] != 1:
                answer += self.n_choose_2(items[1])

        return answer

    def n_choose_2(self, n):
        return (n * (n - 1))/2


    def helper(self, domino_1, domino_2):
        if domino_1 == domino_2:
            return True
        return domino_1[1] == domino_2[0] and domino_1[0] == domino_2[1]

dominoes = [[1,2],[2,1],[3,4],[5,6]]
answer1 = 1

dominoes2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]
answer2 = 3

test_cases = [dominoes, dominoes2]
test_answers = [answer1, answer2]

tests = list(zip(test_cases, test_answers))
solution = Solution()

result = True
for test in tests:
    result = result and (solution.numEquivDominoPairs(test[0]) == test[1])

print(result)
