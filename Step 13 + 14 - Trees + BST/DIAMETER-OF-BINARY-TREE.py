from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def helper(node: Optional[TreeNode]) -> int:
            nonlocal ans
            if not node:
                return 0
            l = helper(node.left)
            r = helper(node.right)
            ans = max(ans, l + r)
            return 1 + max(l, r)

        helper(root)
        return ans
