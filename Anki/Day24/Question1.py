from typing import *

class TrieNode:
    def __init__(self):
        self.neighbours = {}
        self.isEnd = False

    def set_end(self):
        self.isEnd = True

    def contains(self, char):
        if char in self.neighbours:
            return True
        return False

    def add_neighbour(self, char):
        next_trie_node = TrieNode()
        self.neighbours[char] = next_trie_node
        return next_trie_node

    def get_neighbour(self, char):
        return self.neighbours[char]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def find(self, word: str) -> TrieNode:
        head = self.root
        for char in word:
            if not head.contains(char):
                head = head.add_neighbour(char)
            else:
                head = head.get_neighbour(char)
        return head

    def insert(self, word: str) -> None:
        head = self.find(word)
        head.set_end()

    def search(self, word: str) -> bool:
        head = self.root
        for char in word:
            if not head.contains(char):
                return False
            head = head.get_neighbour(char)
        return head.isEnd


    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for char in prefix:
            if not head.contains(char):
                return False
            head = head.get_neighbour(char)
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)