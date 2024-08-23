from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            return max(left, right) + 1

        return helper(root)
