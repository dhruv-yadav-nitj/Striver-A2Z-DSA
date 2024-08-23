class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    # Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        if not head:
            return None
        prev = head
        curr = head.next
        while curr:
            while curr and curr.data == prev.data:
                curr = curr.next
            prev.next = curr
            if curr:
                curr.prev = prev
                prev = curr
                curr = curr.next
        return head
