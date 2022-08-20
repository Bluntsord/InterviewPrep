import time
from typing import *
import queue as q
class Wrapper(object):
    def __init__(self, curr, third, forth):
        self.x = curr[0]
        self.y = curr[1]
        self.third = third
        self.forth = forth

    def __lt__(self, other):
        return self.third < other.third

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        start = Wrapper((0, 0), 0, 0)
        visited = {start: 0}
        queue = q.PriorityQueue()
        queue.put(start)
        answer = 0
        target = (x, y)
        while not queue.empty():
            temp = queue.get()
            curr_node, distance, steps = (temp.x, temp.y), temp.third, temp.forth
            neighbours = self.get_knight_directions(curr_node)

            for neighbour in neighbours:
                if neighbour not in visited:
                    visited[neighbour] = answer
                    if neighbour[0] == x and neighbour[1] == y:
                        return steps + 1
                    euclid_distance = (x - neighbour[0]) ** 2 + (y - neighbour[1]) ** 2
                    next_neighbour = Wrapper(neighbour, euclid_distance, steps + 1)
                    queue.put(next_neighbour)
        answer += 1

        return answer + 1

    def get_knight_directions(self, curr):
        directions = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]
        answer = list(map(lambda x: (curr[0] + x[0], curr[1] + x[1]), directions))
        return answer

    def get_euclid_distance(self, target, curr):
        return (target[0] - curr[0]) ** 2 + (target[1] - curr[1]) ** 2


solution = Solution()
# print(solution.minKnightMoves(1, 2))
# print(solution.minKnightMoves(2, 1))
# print(solution.minKnightMoves(3, 3))

curr = time.time()
print(solution.minKnightMoves(401, 7))
end = time.time()
print(end - curr)