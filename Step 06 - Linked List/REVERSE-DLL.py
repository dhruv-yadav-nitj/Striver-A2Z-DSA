class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    def reverseDLL(self, head):
        if not head or not head.next:
            return head
        prev, curr, next = None, head, head.next
        while curr:
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
            if curr:
                next = curr.next
        return prev

