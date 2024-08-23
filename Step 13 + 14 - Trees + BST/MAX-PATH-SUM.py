import sys
from typing import Optional


# DP on Trees

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = -sys.maxsize

        def helper(curr: Optional[TreeNode]) -> int:
            if not curr:
                return 0
            nonlocal maxi
            left = helper(curr.left)
            right = helper(curr.right)
            this = curr.val
            maxi = max(maxi, this, this + left, this + right, this + left + right)
            return max(this + left, this + right, this)

        temp = helper(root)
        return maxi
