from typing import List

"""
Can buy multiple stocks but can hold only one at a time.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = -1
        profit = 0
        n = len(prices)
        i = 0
        while i < n:
            if buy == -1:
                while i + 1 < n and prices[i + 1] <= prices[i]:
                    i += 1
                buy = prices[i]
            else:
                while i + 1 < n and prices[i + 1] >= prices[i]:
                    i += 1
                if i < n:
                    profit += (prices[i] - buy)
                    buy = -1
            i += 1
        return profit
