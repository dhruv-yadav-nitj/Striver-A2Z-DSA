from typing import List


class Solution:
    def isSubsetSum(self, n: int, arr: List[int], target: int):
        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]

        def memo(ind: int, rem: int) -> bool:
            if ind == n:
                return True if rem == 0 else False
            if rem == 0:
                return True
            if dp[ind][rem] != -1:
                return bool(dp[ind][rem])
            pick = notpick = 0
            if arr[ind] <= rem:
                pick = memo(ind + 1, rem - arr[ind])
            notpick = memo(ind + 1, rem)
            dp[ind][rem] = pick or notpick
            return bool(dp[ind][rem])

        def tabulation():
            dpp = [[False for _ in range(target + 1)] for _ in range(n)]
            for i in range(n):
                dpp[i][0] = True
            if arr[0] <= target:
                dpp[0][arr[0]] = True
            for level in range(1, n):
                for summ in range(1, target + 1):
                    notpick = dpp[level - 1][summ]
                    pick = False
                    if arr[level] <= summ:
                        pick = dpp[level - 1][summ - arr[level]]
                    dpp[level][summ] = pick or notpick
            return dpp[n - 1][target]

        return tabulation()
