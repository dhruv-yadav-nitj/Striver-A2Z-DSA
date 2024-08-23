class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


def countNodesinLoop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            curr = slow.next
            count = 1
            while curr != slow:
                count += 1
                curr = curr.next
            return count
    return 0

