from typing import List


class Solution:
    def selectionSort(self, arr: List[int], n: int):
        for i in range(n):
            mini = i
            for j in range(i, n):
                if arr[j] < arr[mini]:
                    mini = j
            arr[i], arr[mini] = arr[mini], arr[i]
        return arr
