from typing import *

class Solution:
    def solution(self, word, cost):
        left_pointer = right_pointer = 0
        letter_dict = {}
        answer = 0
        while right_pointer < len(word):
            right_letter = word[right_pointer]
            left_letter = word[left_pointer]
            curr_cost = cost[right_pointer]
            while left_letter == right_letter and right_pointer < len(word):
                next_letter = word[right_pointer]
                if cost[right_pointer] > curr_cost:
                    curr_cost = min(curr_cost, cost[right_pointer])
                right_pointer += 1
            right_pointer += 1
            left_pointer += 1
            answer += curr_cost
        return answer

solution = Solution()
s1 = "abccbd"
c1 = [0,1,2,3,4,5]

print(solution.solution(s1, c1))