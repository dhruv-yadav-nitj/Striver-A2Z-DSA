from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(curr: Optional[TreeNode]) -> Optional[TreeNode]:
            if not curr:
                return None
            if curr.val == val:
                return curr
            if val < curr.val:
                return helper(curr.left)
            else:
                return helper(curr.right)

        return helper(root)
