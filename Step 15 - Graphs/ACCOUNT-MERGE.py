from typing import List
from collections import defaultdict


# Just take hint from starting 2-3 lines and you would automatically understand that!
# https://takeuforward.org/data-structure/accounts-merge-dsu-g-50/


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dset = DisjointSet(n)
        mp = defaultdict()
        for i in range(n):
            for mail in accounts[i][1:]:
                if mail in mp:
                    u = mp[mail]
                    v = i
                    dset.union_by_rank(u, v)
                else:
                    mp[mail] = i
        mails = defaultdict(set)
        for i in range(n):
            parent = dset.find_parent(i)
            for mail in accounts[i][1:]:
                mails[parent].add(mail)
        ans = []
        for key, value in mails.items():
            curr = [accounts[key][0]]
            curr.extend(sorted(list(value)))
            ans.append(curr)
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
