from typing import List
from queue import Queue


class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        for u, v in pre:
            adj[u].append(v)
            indegree[v] += 1
        q = Queue()
        for i in range(n):
            if indegree[i] == 0:
                q.put(i)
        ans = []
        while not q.empty():
            curr = q.get()
            ans.append(curr)
            for v in adj[curr]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.put(v)
        return len(ans) == n
