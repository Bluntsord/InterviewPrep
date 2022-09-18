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