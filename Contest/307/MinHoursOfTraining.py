from typing import *


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:

        energy_needed = sum(energy) + 1 - initialEnergy
        # print(energy_needed)
        exp_needed = 0
        for curr_exp in experience:
            if initialExperience <= curr_exp:
                exp_needed += (curr_exp + 1 - initialExperience)
                initialExperience = curr_exp + 1
            else:
                initialExperience += curr_exp
        return exp_needed + energy_needed

initialEnergy = 5
initialExperience = 3
energy = [1,4,3,2]
experience = [2,6,3,1]

solution = Solution()
print(solution.minNumberOfHours(initialEnergy, initialExperience, energy, experience))
