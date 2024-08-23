from typing import List


class Solution:
    def findPath(self, grid: List[List[int]]) -> List[str]:
        n = len(grid)

        if n == 1:
            return []

        ans = []

        def helper(i: int, j: int, path: str):
            if i == n - 1 and j == n - 1 and grid[i][j] == 1:
                ans.append(path)
                return
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                row = [-1, 0, 1, 0]
                col = [0, 1, 0, -1]
                dir = ['U', 'R', 'D', 'L']
                grid[i][j] = 0
                for k in range(4):
                    helper(i + row[k], j + col[k], path + dir[k])
                grid[i][j] = 1
            else:
                return

        helper(0, 0, "")
        return ans
