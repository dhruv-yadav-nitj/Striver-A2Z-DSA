from typing import List


class Solution:
    def cutRod(self, price: List[int], n: int):
        dp = [[-1 for _ in range(n + 1)] for _ in range(n)]

        def memo(i: int, rem: int) -> int:
            if i == n or rem == 0:
                return 0
            if dp[i][rem] != -1:
                return dp[i][rem]
            notpick = 0 + memo(i + 1, rem)
            pick = 0
            if i + 1 <= rem:
                pick = price[i] + memo(i, rem - (i + 1))
            dp[i][rem] = max(pick, notpick)
            return dp[i][rem]

        return memo(0, n)
