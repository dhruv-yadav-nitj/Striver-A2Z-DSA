import heapq
from typing import List
from collections import defaultdict, Counter
from sortedcontainers import SortedDict


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counts = Counter(nums)
        heapq.heapify(nums)
        mp = defaultdict(int, counts)
        print(mp)
        while len(nums):
            curr = heapq.heappop(nums)
            print(curr)
            if curr in mp:
                for i in range(curr, curr + k):
                    if i in mp:
                        mp[i] -= 1
                        if mp[i] == 0:
                            mp.pop(i)
                    else:
                        return False
        return True


# BRUTE FORCE -> USING SortedDict (Hashtable)
class Solution1:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k:
            return False
        mp = SortedDict(Counter(nums))
        while len(mp):
            for key, value in mp.items():
                curr = key
                for i in range(curr, curr + k):
                    if i in mp:
                        mp[i] -= 1
                        if mp[i] == 0:
                            mp.pop(i)
                    else:
                        return False
                break
        return True
