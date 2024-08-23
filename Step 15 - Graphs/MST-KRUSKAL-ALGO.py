from typing import List


class Solution:
    def spanningTree(self, n: int, adj: List[List[int]]):
        edges = []
        for i in range(n):
            for v, wt in adj[i]:
                edges.append((i, v, wt))
        edges.sort(key=lambda x: x[2])
        mst = 0
        dset = DisjointSet(n)
        for u, v, wt in edges:
            pu = dset.find_parent(u)
            pv = dset.find_parent(v)
            if pu != pv:
                mst += wt
                dset.union_by_rank(u, v)
        return mst


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
