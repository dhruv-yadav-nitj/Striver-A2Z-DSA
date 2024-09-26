from typing import List, Optional

# Asked in Accolite Interviews


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        def helper(s: int, e: int) -> Optional[TreeNode]:
            if e <= s:
                return None
            m = (s + e)//2
            curr = TreeNode(nums[m])
            curr.left = helper(s, m)
            curr.right= helper(m+1, e)
            return curr
        return helper(0, n)

