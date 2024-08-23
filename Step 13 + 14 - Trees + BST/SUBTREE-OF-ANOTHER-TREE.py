from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        def helper(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if not node1 and not node2:
                return True
            if not (node1 and node2):
                return False
            if node1.val != node2.val:
                return False
            return helper(node1.left, node2.left) and helper(node1.right, node2.right)

        def dfs(node: Optional[TreeNode]):
            if not node:
                return False
            if node.val == subroot.val:
                if helper(node, subroot):
                    return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
