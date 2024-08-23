from typing import Optional


# PRE-REQUISITE: FLATTEN LINKED LIST
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def gettail(self, head):
        if not head or not head.next:
            return head
        while head.next:
            head = head.next
        return head

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        curr = next = None
        curr = head
        while curr:
            if curr.child is None:
                curr = curr.next
            else:
                next = curr.next
                temp = curr.child
                curr.child = None
                childhead = self.flatten(temp)
                childtail = self.gettail(childhead)
                curr.next = childhead
                childhead.prev = curr
                childtail.next = next
                if next:
                    next.prev = childtail
                curr = next

        return head
