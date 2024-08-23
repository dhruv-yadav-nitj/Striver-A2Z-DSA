from typing import List
from queue import PriorityQueue


class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v, wt in edges:
            adj[u].append((v, wt))
        distance = [int(1e9) for _ in range(n)]
        pq = PriorityQueue()
        pq.put((0, 0))  # src = 0
        distance[0] = 0
        while not pq.empty():
            dist, curr = pq.get()
            for v, wt in adj[curr]:
                if distance[v] > dist + wt:
                    distance[v] = dist + wt
                    pq.put((distance[v], v))
        for i in range(n):
            if distance[i] == int(1e9):
                distance[i] = -1
        return distance
