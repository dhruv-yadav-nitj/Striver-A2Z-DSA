from typing import List

m = int(1e9)


class Solution:
    def minimumEnergy(self, height: List[int], n: int):
        dp = [-1 for _ in range(n)]

        def memoization(ind: int):
            if ind == 0:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            choice1 = abs(height[ind - 1] - height[ind]) + memoization(ind - 1)
            choice2 = m
            if ind > 1:
                choice2 = abs(height[ind - 2] - height[ind]) + memoization(ind - 2)
            dp[ind] = min(choice1, choice2)
            return dp[ind]

        def tabulation(ind: int):
            dpp = [0 for _ in range(n)]
            dpp[0] = 0
            if n > 1:
                dpp[1] = abs(height[1] - height[0])
            for i in range(2, n):
                choice1 = abs(height[i] - height[i - 1]) + dpp[i - 1]
                choice2 = abs(height[i] - height[i - 2]) + dpp[i - 2]
                dpp[i] = min(choice1, choice2)
            return dpp[n - 1]

        return tabulation(n - 1)
