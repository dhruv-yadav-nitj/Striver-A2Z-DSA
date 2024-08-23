from typing import Optional


class TrieNode:
    def __init__(self, data: str = '#'):
        self.data = data
        self.isTerminal = False
        self.children = [Optional[TrieNode] for _ in range(26)]
        for i in range(26):  # initially every child is NULL
            self.children[i] = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        n = len(word)
        curr = self.root
        i = 0
        while i < n:
            index = ord(word[i]) - ord('a')
            if curr.children[index]:
                curr = curr.children[index]
            else:
                curr.children[index] = TrieNode(word[i])
                curr = curr.children[index]
            i += 1
        curr.isTerminal = True

    def search(self, word: str) -> bool:
        n = len(word)
        curr = self.root
        i = 0
        while i < n:
            index = ord(word[i]) - ord('a')
            if curr.children[index]:
                curr = curr.children[index]
            else:
                return False
            i += 1
        return curr.isTerminal

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        curr = self.root
        i = 0
        while i < n:
            index = ord(prefix[i]) - ord('a')
            if curr.children[index]:
                curr = curr.children[index]
            else:
                return False
            i += 1
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
