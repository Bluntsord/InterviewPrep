import functools
from typing import *
from queue import PriorityQueue

class Wrapper:
    def __init__(self, number):
        self.number = number

    def __lt__(self, other):
        current = [x for x in str(self.number)]
        other = [x for x in str(other.number)]

        i = 0
        while i < len(current) and i < len(other):
            curr_int = current[i]
            other_int = other[i]

            if curr_int < other_int:
                return True
            i += 1
        return len(current) > len(other)

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        queue = PriorityQueue()
        for num in nums:
            curr_num = Wrapper(num)
            queue.put(curr_num)

        answer = []
        while not queue.empty():
            curr = queue.get()
            answer.append(curr.number)
        print(answer)
        answer.reverse()
        answer = functools.reduce(lambda x, y: str(x) + str(y), answer)
        return answer

nums = [3,30,34,5,9]
solution = Solution()
print(solution.largestNumber(nums))




