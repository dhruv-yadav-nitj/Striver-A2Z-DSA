from typing import List
from collections import defaultdict
from functools import reduce


# USING EXTRA SPACE
class Solution1:
    def findTwoElement(self, arr: List[int], n: int):
        mp = defaultdict(int, {key: arr.count(key) for key in set(arr)})
        a = b = None
        for i in range(1, n + 1):
            if mp[i] == 2:
                a = i
            if i not in mp or not mp[i]:
                b = i
        return [a, b]


# T.C: O(nlogn + n)
class Solution2:
    def findTwoElement(self, arr, n):
        arr.sort()
        temp, rep, mis = sum(arr), None, None
        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                rep = arr[i]
                break
        temp -= rep
        mis = (n * (n + 1) // 2) - temp
        return [rep, mis]


# METHOD 3 : USING MATHS
class Solution3:
    def findTwoElement(self, arr, n):
        s = sum(arr)
        sn = (n * (n + 1)) // 2
        sn2 = (n * (n + 1) * (2 * n + 1)) // 6
        s2 = sum(list(map(lambda x: x * x, arr)))
        v1 = s - sn
        v2 = (s2 - sn2) // v1
        return [(v1 + v2) // 2, ((v1 + v2) // 2 - v1)]
