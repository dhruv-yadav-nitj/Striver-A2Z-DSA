from typing import List


class Solution:
    def topoSort(self, n: int, adj: List[List[int]]):
        isVisited = [0 for _ in range(n)]
        stack = []

        def dfs(node):
            isVisited[node] = 1
            for v in adj[node]:
                if not isVisited[v]:
                    dfs(v)
            stack.append(node)

        for i in range(n):
            if not isVisited[i]:
                dfs(i)

        return stack[::-1]
