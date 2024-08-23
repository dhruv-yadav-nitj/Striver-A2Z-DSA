from typing import List


class Solution:
    def solve(self, n: int, m: int, grid: List[List[int]]):

        def out_of_bounds(j):
            return j < 0 or j >= m

        def recursion(i1, i2, j1, j2) -> int:
            if out_of_bounds(j1) or out_of_bounds(j2):
                return 0
            if i1 == n - 1 or i2 == n - 1:
                if j1 == j2:
                    return grid[i1][j1]
                else:
                    return grid[i1][j1] + grid[i2][j2]
            maxi = 0
            for k1 in range(-1, 2):
                for k2 in range(-1, 2):
                    if j1 == j2:
                        maxi = max(maxi, grid[i1][j1] + recursion(i1 + 1, i2 + 1, j1 + k1, j2 + k2))
                    else:
                        maxi = max(maxi, grid[i1][j1] + grid[i2][j2] + recursion(i1 + 1, i2 + 1, j1 + k1, j2 + k2))
            return maxi

        # return recursion(0, 0, 0, m - 1)

        dp = [[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]

        # since i1 and i2  would always be same bcz both the robots would always be at the same level! -> 3d DP
        def memoization(i, j1, j2) -> int:
            if out_of_bounds(j1) or out_of_bounds(j2):
                return 0
            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]
            if i == n - 1:
                if j1 == j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]
            maxi = 0
            for k1 in range(-1, 2):
                for k2 in range(-1, 2):
                    if j1 == j2:
                        maxi = max(maxi, grid[i][j1] + memoization(i + 1, j1 + k1, j2 + k2))
                    else:
                        maxi = max(maxi, grid[i][j1] + grid[i][j2] + memoization(i + 1, j1 + k1, j2 + k2))
            dp[i][j1][j2] = maxi
            return maxi

        return memoization(0, 0, m - 1)
