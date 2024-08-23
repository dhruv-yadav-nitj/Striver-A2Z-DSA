from typing import List


class Solution:
    def dfsOfGraph(self, v: int, adj: List[List[int]]):
        ans = []
        isVisited = [0 for _ in range(v)]

        def dfs(node: int):
            ans.append(node)
            isVisited[node] = 1
            for item in adj[node]:
                if not isVisited[item]:
                    dfs(item)
            return None

        dfs(0)
        return ans
