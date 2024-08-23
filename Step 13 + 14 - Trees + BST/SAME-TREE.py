from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1 and not node2:
                return True
            elif not (node1 and node2):
                return False
            else:
                if node1.val == node2.val:
                    return helper(node1.left, node2.left) and helper(node1.right, node2.right)
                else:
                    return False

        return helper(p, q)
