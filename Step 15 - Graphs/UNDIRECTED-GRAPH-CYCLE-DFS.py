from typing import List


class Solution:
    def isCycle(self, v: int, adj: List[List[int]]) -> bool:
        isVisited = [0 for _ in range(v)]

        def dfs(parent, node) -> bool:
            nonlocal isVisited
            isVisited[node] = 1
            for item in adj[node]:
                if not isVisited[item]:
                    if dfs(node, item):
                        return True
                else:
                    if item != parent:
                        return True
            return False

        for i in range(v):
            if not isVisited[i]:
                if dfs(-1, i):
                    return True
        return False
