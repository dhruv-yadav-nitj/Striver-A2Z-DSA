from typing import List, Optional
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = Queue()
        if not root:
            return []
        q.put(root)
        level = []
        while not q.empty():
            size = q.qsize()
            curr_level = []
            while size:
                node: Optional[TreeNode] = q.get()
                curr_level.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                size -= 1
            level.append(curr_level)
        return level
