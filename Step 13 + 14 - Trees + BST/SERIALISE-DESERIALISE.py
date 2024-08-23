from typing import Optional
from queue import Queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        seq = []
        q = Queue()
        q.put(root)
        while not q.empty():
            curr: Optional[TreeNode] = q.get()
            if curr:
                seq.append(str(curr.val))
                q.put(curr.left)
                q.put(curr.right)
            else:
                seq.append('#')

        return ','.join(seq)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = Queue()
        q.put(root)
        i = 1
        while not q.empty():
            node = q.get()
            if nodes[i] != '#':
                node.left = TreeNode(int(nodes[i]))
                q.put(node.left)
            i += 1
            if nodes[i] != '#':
                node.right = TreeNode(int(nodes[i]))
                q.put(node.right)
            i += 1

        return root
