from typing import List
from collections import defaultdict


# METHOD 1 : FOR +ve only elements
class Solution1:
    def lenOfLongSubarr1(self, arr: List[int], n, k):
        n, ans, cum = len(arr), 0, 0
        i = j = 0
        while j < n:
            cum += arr[j]
            while i <= j and cum > k:
                ans -= arr[i]
                i += 1
            if cum == k:
                ans = max(ans, j - i + 1)
            j += 1
        return ans


# METHOD 2 : FOR +ve and -ve elements
class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        mp = defaultdict()
        x, ans = 0, 0
        for i in range(n):
            x += arr[i]
            if x == k:
                ans = max(ans, i+1)
            req = x - k
            if req in mp:
                ans = max(ans, i - mp[req])
            if x not in mp:
                mp[x] = i
        return ans
