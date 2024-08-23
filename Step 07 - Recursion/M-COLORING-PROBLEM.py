from typing import List


def graphColoring(edges: List[List[int]], m: int, n: int):
    color = [0 for _ in range(n)]

    def isValid(col: int, node: int) -> bool:
        for i in range(n):
            if edges[node][i] and color[i] == col:
                return False
        return True

    def helper(node: int) -> bool:
        if node == n:
            return True
        for i in range(1, m + 1):
            if isValid(i, node):
                color[node] = i
                if helper(node + 1):
                    return True
                color[node] = 0
        return False

    return helper(0)
