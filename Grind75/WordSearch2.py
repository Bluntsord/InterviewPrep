from typing import *
import queue as q

# Too slow. TLE

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

    def contains_key(self, char):
        return char in self.children

    def get(self, char):
        return self.children[char]

    def put(self, char):
        next = TrieNode()
        self.children[char] = next


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        head = self.root
        for i in range(len(word)):
            if not head.contains_key(word[i]):
                head.put(word[i])
            head = head.get(word[i])

        head.is_end = True

    def search_prefix(self, word):
        head = self.root
        for i in range(len(word)):
            if not head.contains_key(word[i]):
                return None
            head = head.get(word[i])
        return head

    def search(self, word):
        head = self.search_prefix(word)
        return head.is_end

    def startsWith(self, prefix: str) -> bool:
        head = self.search_prefix(prefix)
        return head is not None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.m, self.n = len(board), len(board[0])
        self.directions = [(0, 1), (1, 0), (0, -1 ), (-1, 0)]
        self.board, self.trie = board, Trie()
        self.answer = []
        self.visited = set()

        for word in words:
            self.trie.insert(word)

        for i in range(self.m):
            for j in range(self.n):
                self.visited = set()
                curr_coord = (i, j)
                self.backTracking(curr_coord, board[i][j])

        return list(set(self.answer))

    def backTracking(self, coord, word_so_far):
        head = self.trie.search_prefix(word_so_far)
        if not head:
            return
        elif head.is_end:
            self.answer.append(word_so_far)

        self.visited.add(coord)
        neighbours = self.get_neighbours(coord)
        for neighbour in neighbours:
            next_char = self.board[neighbour[0]][neighbour[1]]
            if not head.contains_key(next_char):
                continue
            elif next_char in self.visited:
                continue

            self.backTracking(neighbour, word_so_far + next_char)

    def is_valid_coord(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        return True

    def get_neighbours(self, coord):
        answer = list(map(lambda x:(coord[0] + x[0], coord[1] + x[1]), self.directions))
        answer = list(filter(self.is_valid_coord, answer))
        return answer


board = [["a", "a"]]
words = ["aaa"]

board1 = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words1 = ["oath","pea","eat","rain","hklf", "hf"]
words2 = ["hklf", "hf"]


solution = Solution()
print(solution.findWords(board, words))