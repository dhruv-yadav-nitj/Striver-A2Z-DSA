from typing import List


class Solution:
    def kthElement(self, arr1: List[int], arr2: List[int], n: int, m: int, k: int):
        i = j = 0
        if k > n + m:
            return -1
        while i < n and j < m:
            k -= 1
            if k == 0:
                return min(arr1[i], arr2[j])
            if arr1[i] <= arr2[j]:
                i += 1
            else:
                j += 1
        while i < n:
            k -= 1
            if k == 0:
                return arr1[i]
            i += 1
        while j < m:
            k -= 1
            if k == 0:
                return arr2[j]
            j += 1
        return -1
