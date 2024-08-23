import sys
from typing import List

"""
Just watch the video for explanation -> I think its very tough to actually
visualise the solution by just seeing the code or reading any article.
"""


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        c = len(cuts)
        dp = [[-1 for _ in range(c + 1)] for _ in range(c + 1)]
        cuts = [0] + cuts + [n]
        cuts.sort()

        def memo(i, j):
            if i > j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            mini = sys.maxsize
            for ind in range(i, j + 1):
                ans = cuts[j + 1] - cuts[i - 1] + memo(i, ind - 1) + memo(ind + 1, j)
                mini = min(mini, ans)
            dp[i][j] = mini
            return mini

        return memo(1, c)
