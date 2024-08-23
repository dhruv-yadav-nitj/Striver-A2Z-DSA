from typing import List
from collections import defaultdict, Counter


# Recursion Based
class Solution1:
    def wordBreak(self, s: str, dic: List[str]) -> bool:
        mp = defaultdict(int, Counter(dic))
        n = len(s)

        def helper(ind: int, words: List[str]):
            if ind == n:
                for word in words:
                    if word not in mp:
                        return False
                return True
            for i in range(ind + 1, n + 1):
                text = s[ind:i]
                words.append(text)
                if helper(i, words):
                    return True
                words.pop()
            return False

        return helper(0, [])
