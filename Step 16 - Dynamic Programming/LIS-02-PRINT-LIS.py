from typing import List

"""
Trace back the dp (2D) array
"""


class Solution:
    def longestIncreasingSubsequence(self, n: int, arr: List[int]):
        dp = [1 for _ in range(n)]
        last = [-1 for _ in range(n)]
        for curr in range(1, n):
            for prev in range(curr):
                if arr[curr] > arr[prev] and dp[curr] < dp[prev] + 1:
                    dp[curr] = dp[prev] + 1
                    last[curr] = prev
        res = maxi = 0
        for i, lis in enumerate(dp):
            if lis > maxi:
                maxi = lis
                res = i
        ans = []
        while res != -1:
            ans.append(arr[res])
            res = last[res]
        return reversed(ans)
