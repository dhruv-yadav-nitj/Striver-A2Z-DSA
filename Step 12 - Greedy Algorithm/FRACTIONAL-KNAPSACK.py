from typing import Optional, List


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


class Solution:
    def fractionalknapsack(self, w: int, arr: List[Optional[Item]], n: int) -> float:
        ratio = []
        for i, item in enumerate(arr):
            val, weight = item.value, item.weight
            ratio.append((i, val / weight))
        ratio.sort(reverse=True, key=lambda x: x[1])
        ans = 0
        for i, rate in ratio:
            if arr[i].weight <= w:
                w -= arr[i].weight
                ans += arr[i].value
            else:
                ans += rate * w
                break
        return ans
