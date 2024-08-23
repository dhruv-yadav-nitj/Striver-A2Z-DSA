from typing import Optional, List
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = Queue()
        if not root:
            return []
        q.put(root)
        ans = []
        while not q.empty():
            size = q.qsize()
            while size:
                curr = q.get()
                if size == 1:
                    ans.append(curr.val)
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
                size -= 1
        return ans
