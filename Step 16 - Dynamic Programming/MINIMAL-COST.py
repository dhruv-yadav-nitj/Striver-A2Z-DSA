from typing import List


class Solution:
    def recursion(self, ind: int, arr: List[int], k: int, n: int):
        if ind == 0:
            return 0
        mini = int(1e9)
        for i in range(1, k + 1):
            if ind - i >= 0:
                mini = min(mini, abs(arr[ind] - arr[ind - i]) + self.recursion(ind - i, arr, k, n))
        return mini

    def minimizeCost(self, arr: List[int], k: int):
        n = len(arr)

        dp = [-1 for _ in range(n)]

        def memoization(ind: int):
            if ind == 0:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            mini = int(1e9)
            for i in range(1, k + 1):
                if ind - i >= 0:
                    mini = min(mini, abs(arr[ind] - arr[ind - i]) + memoization(ind - i))
            dp[ind] = mini
            return mini

        def tabulation():
            dpp = [0 for _ in range(n)]
            dpp[0] = 0
            dpp[1] = abs(arr[1] - arr[0])
            for i in range(2, n):
                mini = int(1e9)
                for j in range(1, k+1):
                    if i - j >= 0:
                        mini = min(mini, abs(arr[i-j] - arr[i]) + dpp[i - j])
                dpp[i] = mini
            return dpp[n - 1]

        return tabulation()
