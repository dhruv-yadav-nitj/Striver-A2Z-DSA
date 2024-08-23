from typing import List
from queue import Queue


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = [[] for _ in range(n)]
        outdegree = [0 for _ in range(n)]
        q = Queue()
        for u in range(n):
            outdegree[u] = len(graph[u])
            if outdegree[u] == 0:
                q.put(u)
            for v in graph[u]:
                adj[v].append(u)
        ans = []
        while not q.empty():
            curr = q.get()
            ans.append(curr)
            for i in adj[curr]:
                outdegree[i] -= 1
                if outdegree[i] == 0:
                    q.put(i)
        return sorted(ans)
