from typing import List


class Solution:
    def spiralOrder(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        top, bot, left, right = 0, n - 1, 0, m - 1
        count, total = 0, n * m
        ans = []
        while count < total:
            # top row
            for j in range(left, right + 1):
                ans.append(grid[top][j])
                count += 1
            if count == total:
                break
            top += 1
            # right col
            for i in range(top, bot + 1):
                ans.append(grid[i][right])
                count += 1
            if count == total:
                break
            right -= 1
            # bottom row
            for j in range(right, left - 1, -1):
                ans.append(grid[bot][j])
                count += 1
            if count == total:
                break
            bot -= 1
            # left col
            for i in range(bot, top-1, -1):
                ans.append(grid[i][left])
                count += 1
            if count == total:
                break
            left += 1
        return ans
