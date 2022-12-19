from typing import *

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_count, d_count = senate.count('R'), senate.count('D')
        r_ban_count, d_ban_count = 0, 0
        banned = set()
        while r_count != 0 and d_count != 0:
            for i in range(len(senate)):
                if r_count == 0 or d_count == 0:
                    return "Radiant" if d_count == 0 else "Dire"
                elif i in banned:
                    continue
                elif senate[i] == "D" and d_ban_count != 0:
                    d_ban_count -= 1
                    banned.add(i)
                    d_count -= 1
                elif senate[i] == "R" and r_ban_count != 0:
                    r_ban_count -= 1
                    banned.add(i)
                    r_count -= 1
                elif senate[i] == "D":
                    r_ban_count += 1
                elif senate[i] == "R":
                    d_ban_count += 1

        print(r_ban_count, d_ban_count)
        return "Radiant" if d_count == 0 else "Dire"






senate_one = "RD"
senate_one_answer = "Radiant"

senate_two = "RDD"
senate_two_answer = "Dire"

senate_three = "DDRRR"
senate_three_answer = "Dire"


solution = Solution()
print(solution.predictPartyVictory(senate_one) == senate_one_answer)
print(solution.predictPartyVictory(senate_two) == senate_two_answer)
print(solution.predictPartyVictory(senate_three) == senate_three_answer)
