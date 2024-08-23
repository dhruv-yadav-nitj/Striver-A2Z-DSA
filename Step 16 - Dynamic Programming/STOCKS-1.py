from typing import List

"""
Can buy and sell only one stock in the entire span.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for price in prices[1:]:
            if price < buy:
                buy = price
            elif price > buy:
                profit = max(profit, price - buy)
        return profit
