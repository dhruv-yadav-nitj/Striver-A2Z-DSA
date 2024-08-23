from typing import List
# PRE-REQ: COUNT INVERSIONS PROBLEM

class Solution:
    def reversePairs(self, arr: List[int]) -> int:
        n = len(arr)
        return self.mergeSort(arr, 0, n - 1)

    def mergeSort(self, arr: List[int], low: int, high: int) -> int:
        if low >= high:
            return 0
        mid = low + ((high - low) // 2)
        ans = self.mergeSort(arr, low, mid) + self.mergeSort(arr, mid + 1, high) + self.merge(arr, low, mid, high)
        return ans

    def merge(self, arr: List[int], low: int, mid: int, high: int) -> int:
        temp, ans = [], 0
        i, j = low, mid + 1
        ######################################
        # SLIGHT MODIFICATION FROM PROBLEM 'Count Inversions'
        while i <= mid and j <= high:
            if arr[i] > 2 * arr[j]:
                ans += (mid + 1 - i)
                j += 1
            else:
                i += 1
        ######################################
        i, j = low, mid + 1
        while i <= mid and j <= high:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= high:
            temp.append(arr[j])
            j += 1
        arr[low:high + 1] = temp[:]
        return ans
