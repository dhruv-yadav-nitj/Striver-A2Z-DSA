from typing import Optional, List


class TrieNode:
    def __init__(self, data: str = '#'):
        self.data = data
        self.children = [Optional[TrieNode] for _ in range(26)]
        for i in range(26):
            self.children[i] = None
        self.isTerminal = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
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

    def search(self, word: str) -> bool:  # used recursion here!
        n = len(word)

        def helper(curr: Optional[TrieNode], s: str, i: int) -> bool:
            if i >= n:
                return curr.isTerminal
            if s[i] == '.':  # since '.' can be matched with any word -> we need to explore all possibilities
                for j in range(26):
                    if curr.children[j] and helper(curr.children[j], s, i + 1):
                        return True
                return False
            else:
                index = ord(s[i]) - ord('a')
                if curr.children[index]:
                    return helper(curr.children[index], s, i + 1)

        return helper(self.root, word, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
