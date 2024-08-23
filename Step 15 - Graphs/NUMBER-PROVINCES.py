from typing import List


class Solution:
    def findCircleNum(self, adj: List[List[int]]) -> int:
        n = len(adj)
        isVisited = [0 for _ in range(n)]

        def dfs(curr: int) -> None:
            isVisited[curr] = 1
            for i in range(n):
                if adj[curr][i] and i != curr and not isVisited[i]:
                    dfs(i)
            return None

        cnt = 0
        for i in range(n):
            if not isVisited[i]:
                cnt += 1
                dfs(i)
        return cnt
