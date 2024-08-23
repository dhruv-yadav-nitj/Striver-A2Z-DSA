from typing import List
from queue import PriorityQueue


# Considering the graph is fully-connected.

class Solution:
    def spanningTree(self, n: int, adj: List[List[int]]):
        pq = PriorityQueue()
        mst = 0
        isVisited = [0 for _ in range(n)]
        pq.put((0, 0))
        while not pq.empty():
            wt, curr = pq.get()
            if not isVisited[curr]:
                isVisited[curr] = 1
                mst += wt
                for v, weight in adj[curr]:
                    if not isVisited[v]:
                        pq.put((weight, v))
        return mst
