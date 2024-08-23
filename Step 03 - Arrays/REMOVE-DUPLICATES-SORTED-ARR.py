from typing import List


class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        i = j = 0
        n = len(arr)
        while i < n and j < n:
            while j < (n-1) and arr[j] == arr[j+1]:
                j += 1
            arr[i] = arr[j]
            i, j = i+1, j+1
        return i
