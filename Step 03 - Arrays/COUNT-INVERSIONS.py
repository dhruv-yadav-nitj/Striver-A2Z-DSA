from typing import List


class Solution:
    def inversionCount(self, arr: List[int], n: int) -> int:
        n = len(arr)
        return self.mergeSort(arr, 0, n-1)

    def mergeSort(self, arr: List[int], low: int, high: int) -> int:
        if low >= high:
            return 0
        mid = low + ((high - low) // 2)
        left = self.mergeSort(arr, low, mid)
        right = self.mergeSort(arr, mid + 1, high)
        ans = self.merge(arr, low, mid, high)
        ans += left + right
        return ans

    def merge(self, arr: List[int], low: int, mid: int, high: int) -> int:
        temp, ans = [], 0
        i, j = low, mid + 1
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                ans += (mid + 1 - i)
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= high:
            temp.append(arr[j])
            j += 1
        arr[low:high+1] = temp[:]
        return ans
