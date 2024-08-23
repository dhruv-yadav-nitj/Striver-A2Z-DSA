from typing import List


class Solution:
    def insertionSort(self, arr: List[int], n: int):
        for i in range(1, n):
            j = i
            while j > 0 and arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -= 1
        return arr
