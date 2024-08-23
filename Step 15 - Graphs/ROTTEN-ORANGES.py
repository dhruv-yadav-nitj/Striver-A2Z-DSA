from typing import List
from queue import Queue


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = Queue()
        row = [-1, 0, 1, 0]
        col = [0, 1, 0, -1]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.put((i, j, 0))
                    grid[i][j] = 0
        ans = 0
        while not q.empty():
            i, j, time = q.get()
            ans = max(ans, time)
            for k in range(4):
                ni = i + row[k]
                nj = j + col[k]
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                    grid[ni][nj] = 0
                    q.put((ni, nj, time + 1))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return ans
