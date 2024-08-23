from typing import List
from collections import defaultdict


class Solution:
    def pageFaults(self, n: int, c: int, pages: List[int]):
        cache, time, count = defaultdict(int), 0, 0
        for item in pages:
            if item in cache:
                cache[item] = time
            else:
                count += 1
                if len(cache) < c:
                    cache[item] = time
                else:
                    lru, t = None, n
                    for key, value in cache.items():
                        if value < t:
                            lru, t = key, value
                    cache.pop(lru)
                    cache[item] = time
            time += 1
        return count
