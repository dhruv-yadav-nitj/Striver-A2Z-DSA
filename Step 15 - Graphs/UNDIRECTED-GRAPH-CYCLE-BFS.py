from typing import List
from queue import Queue


class Solution:
    def isCycle(self, v: int, adj: List[List[int]]) -> bool:
        isVisited = [0 for _ in range(v)]

        def bfs(i: int) -> bool:
            q = Queue()
            q.put((i, -1))
            isVisited[i] = 1
            while not q.empty():
                node, parent = q.get()
                for item in adj[node]:
                    if not isVisited[item]:
                        isVisited[item] = 1
                        q.put((item, node))
                    else:
                        if item != parent:
                            return True
            return False

        for i in range(v):
            if not isVisited[i] and bfs(i):
                return True
        return False