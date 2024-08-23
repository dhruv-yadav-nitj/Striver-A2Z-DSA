from typing import List
from queue import Queue

"""
Graph is bipartite means that no adjacent nodes are of the same color if we try to color all the nodes of the graph
using just two colors! 
"""


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0 for _ in range(n)]

        def bfs(i: int):
            q = Queue()
            q.put((i, 1))
            color[i] = 1
            while not q.empty():
                node, col = q.get()
                pre = lambda x: 1 if x == 2 else 2
                for item in graph[node]:
                    if color[item] == 0:
                        color[item] = pre(col)
                        q.put((item, color[item]))
                    else:
                        if color[item] == col:
                            return False
            return True

        for i in range(n):
            if color[i] == 0:
                if not bfs(i):
                    return False
        return True
