from typing import List
from queue import Queue


class Solution:
    def shortestPath(self, edges: List[List[int]], n: int, m: int, src: int):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        distance = [int(1e9) for _ in range(n)]
        q = Queue()
        q.put(src)
        distance[src] = 0
        while not q.empty():
            curr = q.get()
            for item in adj[curr]:
                item: int
                if distance[item] > 1 + distance[curr]:
                    distance[item] = 1 + distance[curr]
                    q.put(item)
        for i in range(n):
            if distance[i] == int(1e9):
                distance[i] = -1
        return distance
