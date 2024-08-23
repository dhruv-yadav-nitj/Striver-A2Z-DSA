from typing import List
from sys import maxsize

'''
This could be done easily using DP but constraints dont allow! -> But theres no solution to this problem without
/ recursion or DP.
'''


class Solution:
    def minCoins(self, coins: List[int], m: int, v: int):
        dp = [-1 for _ in range(v + 1)]

        def memo(curr: int):
            if curr == 0:
                return 0
            if dp[curr] != -1:
                return dp[curr]
            ans = maxsize
            for i in range(m):
                if coins[i] <= curr:
                    temp = 1 + memo(curr - coins[i])
                    if temp < maxsize and temp < ans:
                        ans = temp
            dp[curr] = ans
            return ans

        ans = memo(v)
        return ans if ans < maxsize else -1
