from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:
        maxi = int(1e9)
        matrix = [[maxi for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    matrix[i][j] = 0
        for u, v, wt in edges:
            matrix[u][v] = matrix[v][u] = wt
        for k in range(n):
            for u in range(n):
                for v in range(n):
                    matrix[u][v] = min(matrix[u][v], matrix[u][k] + matrix[k][v])
        cnt = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if matrix[i][j] <= threshold:
                    cnt[i] += 1
        res = min(cnt)
        ans = 0
        for i, item in enumerate(cnt):
            if item == res:
                ans = i
        return ans
