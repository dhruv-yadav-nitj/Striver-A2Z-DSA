from typing import List
from collections import defaultdict, Counter
from queue import Queue

"""
BFS
"""


class Solution:
    def ladderLength(self, begin: str, end: str, wordList: List[str]) -> int:
        mp = defaultdict(int, Counter(wordList))
        if end not in mp:
            return 0
        distance = defaultdict(int, {item: int(1e9) for item in wordList})
        """
        Use of distance is necessary because without it, it would be giving TLE. Why? -> Because we would be stuck in a
        infinite queue where we would be always inserting the begin word in the queue again and again. But when we would
        use a distance dictionary we would fix that issue!
        """
        q = Queue()
        q.put((begin, 1))
        n = len(begin)
        while not q.empty():
            curr, dis = q.get()
            if curr == end:
                return dis
            for i in range(n):
                for c in range(ord('a'), ord('z') + 1):
                    ch = chr(c)
                    next = curr[:i] + ch + curr[i + 1:]
                    if next in mp and distance[next] > dis + 1:
                        q.put((next, dis + 1))
                        distance[next] = dis + 1
        return 0
