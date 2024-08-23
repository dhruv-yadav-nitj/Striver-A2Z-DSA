from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []

        def helper(curr: Optional[TreeNode]) -> None:
            if not curr:
                return None
            helper(curr.left)
            inorder.append(curr.val)
            helper(curr.right)
            return None

        helper(root)
        return inorder[k - 1]
