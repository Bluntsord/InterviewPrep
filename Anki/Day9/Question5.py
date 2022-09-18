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

    def search(self, word):
        head = self.root
        for i in range(len(word)):
            if not head.contains_key(word[i]):
                return False
            head = head.get(word[i])

        return head.is_end

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for i in range(len(prefix)):
            if not head.contains_key(prefix[i]):
                return False
            head = head.get(prefix[i])

        return True