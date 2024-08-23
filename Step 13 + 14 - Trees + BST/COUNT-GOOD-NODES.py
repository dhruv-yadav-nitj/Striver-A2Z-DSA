from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        cnt = 0

        def dfs(curr: Optional[TreeNode], maxi: int) -> None:
            nonlocal cnt
            if not curr:
                return None
            if curr.val >= maxi:
                cnt += 1
            dfs(curr.left, max(maxi, curr.val))
            dfs(curr.right, max(maxi, curr.val))
            return None

        dfs(root, int(-1e4))  # why 1e4 -> due to lower limit of constraints in problem given
        return cnt
