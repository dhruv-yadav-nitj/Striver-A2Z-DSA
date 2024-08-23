import sys
from typing import List


class Solution:
    def findKRotation(self, arr: List[int], n: int):
        low, high, mini, ind = 0, len(arr)-1, sys.maxsize, None
        while low <= high:
            mid = (low + high)//2
            if arr[low] <= arr[mid]:
                if arr[low] < mini:
                    mini = arr[low]
                    ind = low
                low = mid + 1
            else:
                if arr[mid] < mini:
                    mini = arr[mid]
                    ind = mid
                high = mid - 1
        return ind
