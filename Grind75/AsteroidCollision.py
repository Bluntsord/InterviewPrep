from typing import *


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for asteroid in asteroids[1:]:
            append_curr = True
            while len(stack) != 0 and stack[-1] * asteroid < 0 and asteroid < 0:
                difference = abs(asteroid) - abs(stack[-1])
                if difference > 0:
                    stack.pop()
                elif difference == 0:
                    stack.pop()
                    append_curr = False
                    break
                else:
                    append_curr = False
                    break

            if append_curr:
                stack.append(asteroid)
        return stack

asteroids = [5,10,-5]
asteroids2 = [8,-8]
asteroids = [1,-2,-2,-2]
solution = Solution()
print(solution.asteroidCollision(asteroids))