from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr_color = image[sr][sc]

        if curr_color == color:  # Edge Case
            return image

        n = len(image)
        m = len(image[0])
        row = [-1, 0, 1, 0]
        col = [0, 1, 0, -1]

        def isValid(i, j):
            return 0 <= i < n and 0 <= j < m and image[i][j] == curr_color

        def dfs(i: int, j: int):
            image[i][j] = color
            for k in range(4):
                ni = i + row[k]
                nj = j + col[k]
                if isValid(ni, nj):
                    dfs(ni, nj)
            return None

        dfs(sr, sc)
        return image
