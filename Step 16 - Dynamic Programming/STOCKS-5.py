from typing import List

"""
Buy and sell stock as many as you want but hold only one stock at a time, and after selling a
stock cooldown period is 1 day i.e., you have to wait one day before buying another stock!
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
                profit3 = prices[ind] + memo(ind + 2, 1)
                profit4 = 0 + memo(ind + 1, buy_stats)
            maxi = max(maxi, profit1, profit2, profit3, profit4)
            dp[ind][buy_stats] = maxi
            return maxi

        return memo(0, 1)
