from typing import Optional


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


# BRUTE FORCE APPROACH
def flatten_bruteforce(root):
    arr = []
    while root:
        arr.append(root.data)
        curr = root.bottom
        while curr:
            arr.append(curr.data)
            curr = curr.bottom
        root = root.next
    arr.sort()
    curr = head = Node(-1)
    for item in arr:
        curr.bottom = Node(item)
        curr = curr.bottom
    return head.bottom


# OPTIMISED APPROACH
def merge(head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]:
    if not head1:
        return head2
    if not head2:
        return head1
    curr = dummyHead = Node(-1)
    while head1 and head2:
        if head1.data <= head2.data:
            curr.bottom = Node(head1.data)
            head1 = head1.bottom
        else:
            curr.bottom = Node(head2.data)
            head2 = head2.bottom
        curr = curr.bottom
    if head1:
        curr.bottom = head1
    if head2:
        curr.bottom = head2
    return dummyHead.bottom


def flatten(root):
    if not root or not root.next:
        return root
    root.next = flatten(root.next)
    root = merge(root, root.next)
    return root
