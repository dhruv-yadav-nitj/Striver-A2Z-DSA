from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1 for _ in range(n)] for _ in range(m)]
        top = 0
        bottom = m-1
        left = 0
        right = n-1
        while head:
            # filling the top row
            j = left
            while head and j <= right:
                grid[top][j] = head.val
                head = head.next
                j += 1
            top += 1
            i = top
            while head and i <= bottom:
                grid[i][right] = head.val
                head = head.next
                i += 1
            right -= 1
            j = right
            while head and j >= left:
                grid[bottom][j] = head.val
                head = head.next
                j -= 1
            bottom -= 1
            i = bottom
            while head and i >= top:
                grid[i][left] = head.val
                head = head.next
                i -= 1
            left += 1
        return grid
