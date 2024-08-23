from typing import List

"""
Introduced a txn fee on selling stocks. So just subtract that fee from the profit when selling.
"""


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(n)]

        def memo(ind: int, buy_stats: int) -> int:
            if ind >= n:
                return 0
            if dp[ind][buy_stats] != -1:
                return dp[ind][buy_stats]
            maxi = 0
            profit1 = profit2 = profit3 = profit4 = 0
            if buy_stats:
                profit1 = -prices[ind] + memo(ind + 1, 0)
                profit2 = memo(ind + 1, buy_stats)
            else:
                profit3 = prices[ind] - fee + memo(ind + 1, 1)
                profit4 = 0 + memo(ind + 1, buy_stats)
            maxi = max(maxi, profit1, profit2, profit3, profit4)
            dp[ind][buy_stats] = maxi
            return maxi

        return memo(0, 1)
