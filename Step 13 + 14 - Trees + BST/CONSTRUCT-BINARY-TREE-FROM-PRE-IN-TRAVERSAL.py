from typing import Optional, List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = defaultdict(int, {value: key for key, value in enumerate(inorder)})

        def helper(prestart: int, preend: int, instart: int, inend: int) -> Optional[TreeNode]:
            if prestart > preend or instart > inend:
                return None
            root_index = mp[preorder[prestart]]
            left_length = root_index - instart
            curr: Optional[TreeNode] = TreeNode(preorder[prestart])
            curr.left = helper(prestart + 1, prestart + left_length, instart, root_index - 1)
            curr.right = helper(prestart + left_length + 1, preend, root_index + 1, inend)
            return curr

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
