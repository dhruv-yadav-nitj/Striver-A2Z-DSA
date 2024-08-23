from typing import List
import bisect


class Solution:
    def rowWithMax1s(self, arr: List[List[int]], n: int, m: int):
        maxi, index = 0, -1
        for i in range(n):
            count = m - bisect.bisect_left(arr[i], 1)
            if count > maxi:
                maxi, index = count, i
        return index
