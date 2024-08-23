import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        m = int(1e9)

        def tabulation():
            dpp = [[0 for _ in range(amount + 1)] for _ in range(n)]
            for i in range(amount + 1):
                dpp[0][i] = i // coins[0] if i % coins[0] == 0 else m
            for i in range(1, n):
                for j in range(amount + 1):
                    not_take = dpp[i - 1][j]
                    take = m
                    if coins[i] <= j:
                        take = 1 + dpp[i][j - coins[i]]
                    dpp[i][j] = min(not_take, take)
            return dpp[n - 1][amount]

        def memo(ind: int, rem: int) -> int:
            if ind == n:
                return 0 if rem == 0 else m
            if rem == 0:
                return 0
            if dp[ind][rem] != -1:
                return dp[ind][rem]
            notpick = 0 + memo(ind + 1, rem)
            pick = m
            if coins[ind] <= rem:
                pick = 1 + memo(ind, rem - coins[ind])
            dp[ind][rem] = min(pick, notpick)
            return dp[ind][rem]

        ans = tabulation()
        return -1 if ans == m else ans
