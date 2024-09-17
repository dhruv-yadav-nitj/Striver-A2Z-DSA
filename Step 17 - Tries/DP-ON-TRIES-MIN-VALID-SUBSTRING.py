from typing import List

# https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/description/


class TrieNode:
    def __init__(self, val: str = '#') -> None:
        self.val = val
        self.children = [None for _ in range(26)]
        self.isEnd = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        i = 0
        n = len(word)
        while i < n:
            index = ord(word[i]) - ord('a')
            if curr.children[index] is not None:
                curr = curr.children[index]
            else:
                curr.children[index] = TrieNode(word[i])
                curr = curr.children[index]
            i += 1
        curr.isEnd = True

    def search(self, target: str) -> bool:
        i = 0
        n = len(target)
        curr = self.root
        while i < n:
            index = ord(target[i]) - ord('a')
            if curr.children[index] is not None:
                curr = curr.children[index]
            else:
                return False
            i += 1
        return curr.isEnd

    def helper(self, target: str) -> int:
        n = len(target)
        dp = [-1 for _ in range(n)]

        def memo(curr_index: int) -> int:
            if curr_index >= n:
                return 0
            if dp[curr_index] != -1:
                return dp[curr_index]
            ans = int(1e9)
            curr = self.root
            for j in range(curr_index, n):
                index = ord(target[j]) - ord('a')
                if curr.children[index] is None:
                    break
                else:
                    curr = curr.children[index]
                    t = memo(j + 1)
                    if t != int(1e9):
                        ans = min(ans, t + 1)
            dp[curr_index] = ans
            return ans
        res = memo(0)
        return res if res < int(1e9) else -1


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.helper(target)
