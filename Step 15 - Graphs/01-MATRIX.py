from typing import List
from queue import Queue


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        q = Queue()
        row = [-1, 0, 1, 0]
        col = [0, 1, 0, -1]
        distance = [[int(1e9) for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.put((i, j, 0))
                    distance[i][j] = 0
        while not q.empty():
            i, j, dis = q.get()
            for k in range(4):
                ni = i + row[k]
                nj = j + col[k]
                if 0 <= ni < n and 0 <= nj < m and mat[ni][nj] == 1 and distance[ni][nj] > 1 + dis:
                    q.put((ni, nj, dis + 1))
                    distance[ni][nj] = 1 + dis
        return distance
