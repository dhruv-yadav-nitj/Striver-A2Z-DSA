from typing import List
from queue import Queue


class Solution:
    def bfsOfGraph(self, v: int, adj: List[List[int]]) -> List[int]:
        q = Queue()
        ans = []
        isVisited = [0 for _ in range(v)]
        q.put(0)
        isVisited[0] = 1
        while not q.empty():
            curr = q.get()
            ans.append(curr)
            for item in adj[curr]:
                if not isVisited[item]:
                    q.put(item)
                    isVisited[item] = 1
        return ans
