from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row = [-1, 0, 1, 0]
        col = [0, 1, 0, -1]
        n = len(grid)
        m = len(grid[0])

        def dfs(i: int, j: int) -> None:
            grid[i][j] = -1
            for k in range(4):
                ni = i + row[k]
                nj = j + col[k]
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                    dfs(ni, nj)

        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and grid[i][j] == 1:
                    dfs(i, j)

        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt += 1
        return cnt
