from typing import *

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m, self.n = len(board), len(board[0])
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.memo = {}

        def backTracking(coord, word_so_far):
            if (coord, word_so_far) in self.memo and coord not in visited:
                return self.memo[(coord, word_so_far)]
            curr_word = word_so_far + board[coord[0]][coord[1]]
            if curr_word == word:
                return True
            elif word_so_far + board[coord[0]][coord[1]] != word[:len(word_so_far) + 1]:
                return False

            neighbours = self.get_neighbours(coord)
            answer = False
            for neighbour in neighbours:
                if neighbour in visited:
                    continue
                visited.add(neighbour)

                answer = answer or backTracking(neighbour, curr_word)
                visited.remove(neighbour)

            self.memo[(coord, word_so_far)] = answer
            return answer

        start = []
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    start.append((i, j))

        for start_coord in start:
            visited = set()
            visited.add(start_coord)
            curr = backTracking(start_coord, "")
            if curr:
                return True

        return False

    def get_neighbours(self, coord):
        answer = map(lambda x: (x[0] + coord[0], x[1] + coord[1]), self.directions)
        answer = filter(self.is_valid_square, answer)

        return list(answer)

    def is_valid_square(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        return True


board = [["A","B","E"],
         ["B","C","D"]]
word = "ABCDEB"
solution = Solution()
print(solution.exist(board, word))
