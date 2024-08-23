from typing import List
from queue import Queue

"""
Topo Sort Using Kahn's Algo (BFS)
"""


class Solution:
    def topoSort(self, n: int, adj: List[List[int]]) -> List[int]:
        q = Queue()
        indegree = [0 for _ in range(n)]
        for u in range(n):
            for v in adj[u]:
                indegree[v] += 1
        for u in range(n):
            if indegree[u] == 0:
                q.put(u)
        ans = []
        while not q.empty():
            curr = q.get()
            ans.append(curr)
            for v in adj[curr]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.put(v)
        return ans
