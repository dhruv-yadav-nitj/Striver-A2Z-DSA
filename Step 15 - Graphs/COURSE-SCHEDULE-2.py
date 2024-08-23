from typing import List
from queue import Queue


class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        ans = []
        indegree = [0 for _ in range(n)]
        adj = [[] for _ in range(n)]
        for u, v in pre:
            indegree[u] += 1
            adj[v].append(u)
        q = Queue()
        for i in range(n):
            if indegree[i] == 0:
                q.put(i)
        while not q.empty():
            curr = q.get()
            ans.append(curr)
            for v in adj[curr]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.put(v)
        return ans if len(ans) == n else []
