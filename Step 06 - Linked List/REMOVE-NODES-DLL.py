# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    def deleteAllOccurOfX(self, head, x):
        while head and head.data == x:
            head = head.next
        prev = head
        curr = head.next
        while curr:
            next = curr.next
            if curr.data == x:
                prev.next = next
                if next:
                    next.prev = prev
                curr = next
            else:
                prev = curr
                curr = next
        return head
