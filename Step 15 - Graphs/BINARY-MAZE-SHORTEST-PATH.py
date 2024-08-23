from typing import List
from queue import PriorityQueue


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
            return -1
        distance = [[int(1e9) for _ in range(m)] for _ in range(n)]
        row = [-1, -1, -1, 0, 1, 1, 1, 0]
        col = [-1, 0, 1, 1, 1, 0, -1, -1]

        def isValid(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m and grid[i][j] == 0

        distance[0][0] = 1
        pq = PriorityQueue()
        pq.put((1, 0, 0))
        while not pq.empty():
            dist, i, j = pq.get()
            if i == n - 1 and j == m - 1:
                return dist
            for k in range(8):
                ni = i + row[k]
                nj = j + col[k]
                if isValid(ni, nj) and distance[ni][nj] > dist + 1:
                    distance[ni][nj] = dist + 1
                    pq.put((distance[ni][nj], ni, nj))
        return -1
