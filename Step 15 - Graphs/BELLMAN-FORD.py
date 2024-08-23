from typing import List


class Solution:
    def bellman_ford(self, n: int, edges: List[List[int]], s: int):
        maxi = int(1e8)  # given in problem to keep max limit as 1e8
        distance = [maxi for _ in range(n)]
        distance[s] = 0
        # Bellman Ford's necessary (n-1) iterations
        for i in range(n - 1):
            for u, v, wt in edges:
                if distance[u] != maxi and distance[v] > distance[u] + wt:
                    distance[v] = distance[u] + wt
        # One more iteration to check negative cycle
        negative_cycle = False
        for u, v, wt in edges:
            if distance[u] != maxi and distance[v] > distance[u] + wt:
                negative_cycle = True
                break
        return [-1] if negative_cycle else distance
