from typing import List

'''
Hint: this problem is just a tweaked version of 'Largest Rectangle in Histogram' problem on leetcode.
Here convert this grid into histograms!
'''


class Solution:
    def maximalRectangle(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        grid = [list(map(int, grid[i])) for i in range(n)]
        for i in range(1, n):
            for j in range(m):
                if grid[i][j]:
                    grid[i][j] += grid[i - 1][j]
        maxi = max([self.helper(grid[i]) for i in range(n)])
        return maxi

    def helper(self, row: List[int]) -> int:
        """
        Same function as used in Largest Rectangle in Histogram Solution 3
        """
        stack = []
        n = len(row)
        ans = 0
        for i, h in enumerate(row):
            while len(stack) and h < row[stack[-1]]:
                nse = i
                curr = stack.pop()
                pse = -1
                if len(stack):
                    pse = stack[-1]
                ans = max(ans, (nse - pse - 1) * row[curr])
            stack.append(i)
        while len(stack):
            nse = n
            curr = stack.pop()
            pse = -1
            if len(stack):
                pse = stack[-1]
            ans = max(ans, (nse - pse - 1) * row[curr])
        return ans
