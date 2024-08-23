from typing import Optional


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: Optional[Node], p: Optional[Node], q: Optional[Node]) -> Optional[Node]:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:  # no answer in left part
            return right
        elif not right:  # no answer in right part
            return left
        else:  # got answer in both part
            return root
