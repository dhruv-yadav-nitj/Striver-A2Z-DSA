from typing import List


class Solution:
    def perfectSum(self, arr: List[int], n: int, target: int):
        def tabulation():
            dp = [[0 for _ in range(target + 1)] for _ in range(n+1)]
            for i in range(n+1):
                dp[i][0] = 1
            if arr[0] <= target:
                dp[1][arr[0]] = 1
            for i in range(1, n+1):
                for j in range(1, target + 1):
                    not_taken = dp[i - 1][j]
                    taken = 0
                    if arr[i-1] <= j:
                        taken = dp[i - 1][j - arr[i-1]]
                    dp[i][j] = taken + not_taken
            return dp[n][target]

        return tabulation()


