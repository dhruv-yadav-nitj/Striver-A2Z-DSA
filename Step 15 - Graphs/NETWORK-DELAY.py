from typing import List
from queue import PriorityQueue


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]  # due to problem being given in 1-indexed nodes
        for u, v, wt in times:
            adj[u].append((v, wt))
        pq = PriorityQueue()
        pq.put((0, k))
        time = [int(1e9) for _ in range(n + 1)]
        time[k] = 0
        while not pq.empty():
            t, curr = pq.get()
            for v, wt in adj[curr]:
                if time[v] > t + wt:
                    time[v] = t + wt
                    pq.put((time[v], v))
        ans = max(time[1:])
        return ans if ans < int(1e9) else -1
