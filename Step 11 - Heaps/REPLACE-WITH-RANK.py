from collections import defaultdict
from typing import List

# Not a Heap Problem

class Solution:
    def replaceWithRank(self, n: int, arr: List[int]):
        temp = sorted(arr)
        mp = defaultdict(int)
        k = 1
        for i in range(n):
            if temp[i] not in mp:
                mp[temp[i]] = k
                k += 1
        arr = [mp[item] for item in arr]
        return arr
