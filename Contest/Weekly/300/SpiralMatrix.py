from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        self.m = m
        self.n = n
        self.visited = {}
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.directions_pointer = 0
        self.stack = [(0, 0)]
        self.answer_matrix = [[-1 for _ in range(self.n)] for _ in range(self.m)]

        while len(self.stack) != 0:
            curr = self.stack.pop()
            self.visited[curr] = 1
            self.answer_matrix[curr[0]][curr[1]] = head.val
            head = head.next
            neighbour = self.get_next_direction(curr)
            if head is None:
                continue
            self.stack.append(neighbour)

        return self.answer_matrix

    def is_valid_coord(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n or coord in self.visited:
            return False
        return True

    def get_next_direction(self, coord):
        for i in range(4):
            self.directions_pointer = self.directions_pointer % 4
            next_direction = self.directions[self.directions_pointer]
            next = (coord[0] + next_direction[0], coord[1] + next_direction[1])
            if self.is_valid_coord(next):
                return next
            self.directions_pointer += 1
m = 3
n = 5
temp = [3,0,2,6,8,1,7,9,4,2,5,5,0]
head = ListNode(temp[0])
another_temp = head

for i in range(1, len(temp)):
    number = temp[i]
    another_temp.next = ListNode(number)
    another_temp = another_temp.next
#
# while head is not None:
#     print(head.val)
#     head = head.next


solution = Solution()
print(solution.spiralMatrix(m, n, head))


