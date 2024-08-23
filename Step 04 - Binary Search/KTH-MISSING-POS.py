from typing import List
from collections import defaultdict


# APPROACH 1 : USING O(N) TIME AND SPACE
class Solution1:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        mp = defaultdict(int, {item: 1 for item in arr})
        i = 1
        while k:
            if i not in mp:
                k -= 1
            i += 1
        return i - 1


# APPROACH 2 : O(N) TIME ; O(1) SPACE
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for item in arr:
            if item <= k:
                k += 1
            else:
                break
        return k
