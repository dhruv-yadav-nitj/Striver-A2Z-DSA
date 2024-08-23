from typing import List

'''
Just take some hint : https://youtu.be/lgiz0Oup6gM?si=sLQo3V1Cs8C7jxE1
'''


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dset = DisjointSet(n * m)

        def is_valid(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m and grid[i][j] == 1

        row = [-1, 0, 1, 0]
        col = [0, 1, 0, -1]

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    u = i * m + j
                    for k in range(4):
                        ni = i + row[k]
                        nj = j + col[k]
                        if is_valid(ni, nj):
                            v = ni * m + nj
                            dset.union_by_size(u, v)
        ans = max(dset.size[i] for i in range(n * m))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    u = i * m + j
                    size = 1
                    st = set()
                    for k in range(4):
                        ni = i + row[k]
                        nj = j + col[k]
                        if is_valid(ni, nj):
                            v = ni * m + nj
                            if dset.find_parent(v) not in st:
                                size += dset.size[dset.find_parent(v)]
                                st.add(dset.find_parent(v))
                    ans = max(ans, size)
        return ans


class DisjointSet:
    def __init__(self, n: int):
        self.rank = [0 for _ in range(n)]  # for union-by-rank
        self.size = [1 for _ in range(n)]  # for union-by-size
        self.parent = [i for i in range(n)]

    def find_parent(self, x: int) -> int:
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]

    def union_by_rank(self, u: int, v: int) -> None:
        pu = self.find_parent(u)
        pv = self.find_parent(v)
        if pu == pv:  # if both are already connected
            return None
        if self.rank[pu] >= self.rank[pv]:
            self.parent[pv] = pu
            if self.rank[pu] == self.rank[pv]:
                self.rank[pu] += 1
        else:
            self.parent[pu] = pv
        return None

    def union_by_size(self, u: int, v: int) -> None:
        pu = self.find_parent(u)
        pv = self.find_parent(v)
        if pu == pv:  # if both are already connected
            return None
        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        return None
