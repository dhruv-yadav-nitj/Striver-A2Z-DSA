from typing import List
from collections import defaultdict


class Solution:
    def maxLen(self, n, arr):
        temp, mp = 0, defaultdict(int)
        ans = 0
        for i in range(len(arr)):
            temp += arr[i]
            if temp == 0:
                ans = i+1
            elif temp in mp:
                ans = max(ans, i - mp[temp])
            if temp not in mp:
                mp[temp] = i
        return ans
