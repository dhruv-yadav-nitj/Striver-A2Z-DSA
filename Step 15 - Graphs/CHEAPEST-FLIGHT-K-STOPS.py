from typing import List
from queue import PriorityQueue


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, wt in flights:
            adj[u].append((v, wt))
        ans = int(1e9)
        price = [int(1e9) for _ in range(n)]
        pq = PriorityQueue()
        pq.put((-1, 0, src))
        price[src] = 0
        while not pq.empty():
            stops, cost, curr = pq.get()
            if curr == dst:
                ans = min(ans, cost)
            if stops + 1 <= k:
                for v, wt in adj[curr]:
                    if price[v] > cost + wt:
                        price[v] = cost + wt
                        pq.put((stops + 1, price[v], v))
        return ans if ans < int(1e9) else -1
