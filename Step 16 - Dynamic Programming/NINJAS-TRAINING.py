from typing import List

"""
Marked for revision -> could not understand the logic behind its tabulation approach!
"""

class Solution:
    def maximumPoints(self, arr: List[List[int]], n: int):
        dp = [[-1 for _ in range(n + 1)] for _ in range(n)]

        def memo(prev: int, curr: int):
            if curr == n:
                return 0
            if dp[curr][prev + 1] != -1:
                return dp[curr][prev + 1]
            maxi = -1
            for i in range(3):
                if i != prev:
                    maxi = max(maxi, arr[curr][i] + memo(i, curr + 1))
            dp[curr][prev + 1] = maxi
            return maxi

        # return memo(-1, 0)

        def tabulation():
            dpp = [[-1 for _ in range(4)] for _ in range(n)]
            dpp[0][0] = max(arr[0][1], arr[0][2])
            dpp[0][1] = max(arr[0][0], arr[0][2])
            dpp[0][2] = max(arr[0][0], arr[0][1])
            dpp[0][3] = max(arr[0][0], arr[0][1], arr[0][2])  # which might be the case if n = 1 (single day)
            for curr in range(1, n):
                for last in range(4):
                    maxi = 0
                    for task in range(3):
                        if task != last:
                            maxi = max(maxi, arr[curr][task] + dpp[curr - 1][task])
                    dpp[curr][last] = maxi
            return dpp[n - 1][3]

        return tabulation()
