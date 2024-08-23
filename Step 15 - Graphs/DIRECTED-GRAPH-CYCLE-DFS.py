from typing import List


class Solution:
    def isCyclic(self, n: int, adj: List[List[int]]) -> bool:
        isVisited = [0 for _ in range(n)]
        isSamePath = [0 for _ in range(n)]

        def dfs(node: int) -> bool:
            isVisited[node] = 1
            isSamePath[node] = 1
            for item in adj[node]:
                # Return True when:
                # already visited and same path
                # not visited -> so visit and it returns True
                if (isVisited[item] and isSamePath[item]) or (not isVisited[item] and dfs(item)):
                    return True
            isSamePath[node] = 0
            return False

        for i in range(n):
            if not isVisited[i] and dfs(i):
                return True
        return False
