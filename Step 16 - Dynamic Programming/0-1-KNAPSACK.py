from typing import List


class Solution:
    def knapSack(self, w: int, wt: List[int], val: List[int], n: int):
        dp = [[-1 for _ in range(w + 1)] for _ in range(n)]

        def tabulation():
            dpp = [[0 for _ in range(w + 1)] for _ in range(n)]
            for j in range(wt[0], w + 1):
                dpp[0][j] = val[0]
            for i in range(1, n):
                for j in range(w + 1):
                    not_take = dpp[i - 1][j]
                    take = 0
                    if j >= wt[i]:
                        take = val[i] + dpp[i - 1][w - wt[i]]
                    dpp[i][j] = max(take, not_take)
            return dpp[n - 1][w]

        def memo(ind: int, rem: int) -> int:
            if ind == n or rem == 0:
                return 0
            if dp[ind][rem] != -1:
                return dp[ind][rem]
            notpick = 0 + memo(ind + 1, rem)
            pick = 0
            if wt[ind] <= rem:
                pick = val[ind] + memo(ind + 1, rem - wt[ind])
            dp[ind][rem] = max(pick, notpick)
            return dp[ind][rem]

        return tabulation()
