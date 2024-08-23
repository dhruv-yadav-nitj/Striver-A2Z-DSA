from typing import List


class Solution:
    def knapSack(self, n: int, w: int, val: List[int], wt: List[int]):
        dp = [[-1 for _ in range(w + 1)] for _ in range(n)]

        def tabulation():
            pass

        def memo(ind: int, rem: int) -> int:
            if ind == n or rem == 0:
                return 0
            if dp[ind][rem] != -1:
                return dp[ind][rem]
            notpick = memo(ind + 1, rem)
            pick = 0
            if wt[ind] <= rem:
                pick = val[ind] + memo(ind, rem - wt[ind])
            dp[ind][rem] = max(pick, notpick)
            return dp[ind][rem]

        return memo(0, w)


"""
Dont know whats wrong with gfg but it gives error while executing correct code.
It has occurred to me multiple times that it continuously gives error while
executing memoization code.
"""
