from typing import Optional
from collections import defaultdict


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        mp = defaultdict()
        temp = head
        while temp:
            mp[temp] = Node(temp.val)
            temp = temp.next
        temp = head
        while temp:
            mp[temp].next = mp[temp.next] if temp.next else None
            mp[temp].random = mp[temp.random] if temp.random else None
            temp = temp.next
        return mp[head]

