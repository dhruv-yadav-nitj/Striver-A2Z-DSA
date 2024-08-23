from typing import List

"""
Can do at most 2 transactions and cant hold more than one stack at a time!
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1 for _ in range(2)] for _ in range(2)] for _ in range(n)]
        
        def memo(ind: int, buy_stat: int, cap: int) -> int:
            if cap < 0 or ind >= n:
                return 0
            if dp[ind][cap][buy_stat] != -1:
                return dp[ind][cap][buy_stat]
            maxi = 0
            profit1 = profit2 = profit3 = profit4 = 0
            if buy_stat:
                profit1 = -prices[ind] + memo(ind + 1, 0, cap)
                profit2 = memo(ind + 1, buy_stat, cap)
            else:
                profit3 = prices[ind] + memo(ind + 1, 1, cap - 1)
                profit4 = 0 + memo(ind + 1, buy_stat, cap)
            maxi = max(profit1, profit2, profit3, profit4)
            dp[ind][cap][buy_stat] = maxi
            return maxi

        return memo(0, 1, 1)
        # cap = 1 bcz we shifted origin for cap which now can be 0 or 1 as to accommodate in dp
