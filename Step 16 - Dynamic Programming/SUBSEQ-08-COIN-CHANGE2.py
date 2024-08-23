import sys
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
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
                return 1 if rem == 0 else 0
            if rem == 0:
                return 1
            if dp[ind][rem] != -1:
                return dp[ind][rem]
            notpick = memo(ind + 1, rem)
            pick = 0
            if coins[ind] <= rem:
                pick = memo(ind, rem - coins[ind])
            dp[ind][rem] = pick + notpick
            return dp[ind][rem]

        ans = memo(0, amount)
        return -1 if ans == m else ans
