from typing import List
from queue import PriorityQueue


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        row = [-1, 0, 1, 0]
        col = [0, 1, 0, -1]

        def isValid(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m

        distance = [[int(1e9) for _ in range(m)] for _ in range(n)]
        pq = PriorityQueue()
        pq.put((0, 0, 0))
        distance[0][0] = 0
        while not pq.empty():
            dist, i, j = pq.get()
            if (i, j) == (n - 1, m - 1):
                return dist
            for k in range(4):
                ni = i + row[k]
                nj = j + col[k]
                if isValid(ni, nj):
                    max_wt = max(dist, abs(heights[ni][nj] - heights[i][j]))
                    if distance[ni][nj] > max_wt:
                        distance[ni][nj] = max_wt
                        pq.put((max_wt, ni, nj))
        return distance[n - 1][m - 1]
