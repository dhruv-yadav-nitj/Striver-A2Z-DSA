from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        l = root.left
        r = root.right
        root.left = r
        root.right = l
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
