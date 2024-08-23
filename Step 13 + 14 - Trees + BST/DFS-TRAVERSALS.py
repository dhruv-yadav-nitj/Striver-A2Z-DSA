from typing import Optional


class Node:
    def __init__(self, val: int):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def inorder_traversal(self, root: Optional[Node]):
        inorder = []

        def helper(node: Optional[Node]):
            if not node:
                return
            helper(node.left)
            inorder.append(node.data)
            helper(node.right)

        helper(root)
        return inorder

    def preorder_traversal(self, root: Optional[Node]):
        preorder = []

        def helper(node: Optional[Node]):
            if not node:
                return
            preorder.append(node.data)
            helper(node.left)
            helper(node.right)

        helper(root)
        return preorder

    def postorder_traversal(self, root: Optional[Node]):
        postorder = []

        def helper(node: Optional[Node]):
            if not node:
                return
            helper(node.left)
            helper(node.right)
            postorder.append(node.data)

        helper(root)
        return postorder
