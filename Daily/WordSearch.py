from typing import *
import queue as q

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
        trie = Trie()
        self.m, self.n = len(board), len(board[0])
        for word in words:
            trie.insert(word)
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def backTracking(self, coord):
        queue = q.Queue()
        queue.put(coord)
        visited = {}

        while not queue.empty():
            curr_coord = queue.get()
            neighbours = self.get_neighbours(curr_coord)

            for neighbour in neighbours:
                if neighbour in visited:
                    continue
                visited[neighbour] = curr_coord
                queue.put(neighbour)


    def get_neighbours(self, coord):
        answer = list(map(lambda x: (x[0] + coord[0], x[1] + coord[1])), self.directions)
        answer = list(filter(self.is_valid_coord, answer))

        return answer


    def is_valid_coord(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        return True



