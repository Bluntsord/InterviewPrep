from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        answer = 0
        for i in range(len(brackets)):
            cut_off, percentage = brackets[i][0], brackets[i][1]
            prev = 0 if i == 0 else brackets[i - 1][0]
            curr = cut_off - prev if income > cut_off else income - prev
            curr_additional = curr * percentage/100
            answer += curr_additional
            if income < cut_off:
                break
        return answer

nums = [[1,0],[4,25],[5,50]]
income = 2
solution = Solution()
print(solution.calculateTax(nums, income))