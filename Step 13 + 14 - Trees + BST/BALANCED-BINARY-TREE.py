from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            return 1 + max(l, r)

        def helper(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            dl = depth(node.left)
            dr = depth(node.right)
            if abs(dr - dl) > 1:
                return False
            return helper(node.left) and helper(node.right)

        return helper(root)
