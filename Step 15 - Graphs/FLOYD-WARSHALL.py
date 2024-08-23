from typing import List


class Solution:
    def shortest_distance(self, matrix: List[List[int]]):
        n = len(matrix)
        maxi = int(1e9)
        # Modify the non-reachable edges (which are -1 by default)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = maxi
                if i == j:  # distance from node to itself is zero always (important)
                    matrix[i][j] = 0
        # Calculating shortest distance b/w each pair of nodes
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        # Place -1 for the nodes which are unreachable from each other
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == maxi:
                    matrix[i][j] = -1
