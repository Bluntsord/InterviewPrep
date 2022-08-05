from typing import *

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.m = len(board)
        self.n = len(board[0])
        self.solved = False
        self.starting = []
        self.visited = {}

        self.avail_letters = {}

        for i in range(self.m):
            for j in range(self.n):
                curr = self.board[i][j]
                if curr == word[0]:
                    temp = (i, j)
                    self.starting.append(temp)
                if curr not in self.avail_letters:
                    self.avail_letters[curr] = 1

        for char in self.word:
            if char not in self.avail_letters:
                return False

        for coord in self.starting:
            self.visited.clear()
            self.visited[coord] = 1
            self.backTracking(coord, word[0])
            if self.solved:
                break

        return self.solved

    def backTracking(self, coord, acc):
        if self.solved:
            return
        elif coord is None:
            return
        elif acc == self.word:
            self.solved = True
            return
        elif acc != self.word[:len(acc)]:
            return

        neighbours = self.get_neighbours(coord)
        for neighbour in neighbours:
            if neighbour in self.visited:
                continue
            curr_letter = self.board[neighbour[0]][neighbour[1]]
            self.visited[neighbour] = 1
            acc += curr_letter
            self.backTracking(neighbour, acc)
            self.visited.pop(neighbour)
            acc = acc.removesuffix(curr_letter)

    def get_neighbours(self, coord):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        answer = list(map(lambda x: (x[0] + coord[0], x[1] + coord[1]), directions))
        answer = list(filter(self.is_valid_square, answer))
        return answer

    def is_valid_square(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        return True


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABC"
board2 = [["a", "a"]]
word2 = "aaa"
solution = Solution()
print(solution.exist(board2, word2))