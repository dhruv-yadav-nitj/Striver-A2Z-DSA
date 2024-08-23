from typing import List
from queue import PriorityQueue
import sys


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        pq = PriorityQueue()
        adj = [[] for _ in range(n)]
        for u, v, wt in roads:
            adj[u].append((v, wt))
            adj[v].append((u, wt))
        distance = [sys.maxsize for _ in range(n)]  # sys.maxsize bcz it was the upper limit in the problem!
        distance[0] = 0
        pq.put((0, 0))
        ways = [1 for _ in range(n)]
        while not pq.empty():
            cost, curr = pq.get()
            for v, wt in adj[curr]:
                if distance[v] > cost + wt:
                    distance[v] = cost + wt
                    pq.put((distance[v], v))
                    ways[v] = ways[curr]
                elif distance[v] == cost + wt:
                    ways[v] += ways[curr]
        return ways[n - 1] % int(1e9 + 7)
