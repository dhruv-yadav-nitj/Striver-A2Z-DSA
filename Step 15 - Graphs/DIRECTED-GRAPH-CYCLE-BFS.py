"""
Using Topo Sort Concept
"""
from typing import List
from queue import Queue


class Solution:
    def isCyclic(self, n: int, adj: List[List[int]]) -> bool:
        indegree = [0 for _ in range(n)]
        for u in range(n):
            for v in adj[u]:
                indegree[v] += 1
        q = Queue()
        for i in range(n):
            if indegree[i] == 0:
                q.put(i)
        topo = []
        while not q.empty():
            node = q.get()
            topo.append(node)
            for v in adj[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.put(v)
        return len(topo) != n
