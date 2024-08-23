from typing import List

'''
Concept:
Nodes which have same parent are already connected so the edge between them would be counted as extra cable.
At last the number of ultimate parents (independent nodes) need to be connected together.
So we can connect 'n' nodes with 'n-1' cables.
'''


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dset = DisjointSet(n)
        cables = len(connections)
        req = extra = 0
        for u, v in connections:
            if dset.union_by_size(u, v):
                extra += 1
        for par, i in enumerate(dset.parent):
            if par == i:
                req += 1
        return req - 1 if req - 1 <= extra else -1


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

    def union_by_rank(self, u: int, v: int) -> int:
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
            return 1
        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        return 0
