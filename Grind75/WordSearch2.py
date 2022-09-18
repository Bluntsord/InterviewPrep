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
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        self.trie = Trie()
        self.visited = {}
        self.answer = []
        for word in words:
            self.trie.insert(word)
        self.first_letter_coord = {word[0]: 1 for word in words}
        self.word_len_dict = {len(word) for word in words}
        self.max_length = max(self.word_len_dict)
        self.word_dict = {}

        for word in words:
            temp = self.word_dict.get(word[0], set())
            temp.add(word)
            self.word_dict[word[0]] = temp


        for i in range(self.m):
            for j in range(self.n):
                if len(self.word_dict.get(word[0])) == 0:
                    continue
                if board[i][j] in self.first_letter_coord and self.trie.search_prefix(board[i][j]) is not None:
                    self.visited = {}
                    self.backTracking((i, j), board[i][j])

        self.answer = list(set(self.answer))
        return self.answer

    def backTracking(self, coord, word):
        head = self.trie.search_prefix(word)
        if head is None:
            return
        elif head.is_end:
            temp = self.word_dict.get(word[0])
            print(temp)
            temp.remove(word)
            print(temp)
            print("==")
            self.word_dict[word[0]] = temp
            self.answer.append(word)

        if len(word) >= self.max_length:
            return

        neighbours = self.get_neighbours(coord)
        for neighbour in neighbours:
            if neighbour in self.visited:
                continue
            next_word = word + self.board[neighbour[0]][neighbour[1]]
            self.visited[coord] = 1

            self.backTracking(neighbour, next_word)
            self.visited.pop(coord)


    def is_valid_coord(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        return True

    def get_neighbours(self, coord):
        answer = list(map(lambda x:(coord[0] + x[0], coord[1] + x[1]), self.directions))
        answer = list(filter(self.is_valid_coord, answer))
        return answer


board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

board1 = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words1 = ["oath","pea","eat","rain","hklf", "hf"]
words2 = ["hklf", "hf"]


solution = Solution()
print(solution.findWords(board1, words2))