from typing import Optional
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low = -sys.maxsize
        high = sys.maxsize

        def helper(curr: Optional[TreeNode], left: int, right: int) -> bool:
            if not curr:
                return True
            if left < curr.val < right:
                l = helper(curr.left, left, curr.val)
                r = helper(curr.right, curr.val, right)
                return l and r
            else:
                return False

        return helper(root, low, high)
