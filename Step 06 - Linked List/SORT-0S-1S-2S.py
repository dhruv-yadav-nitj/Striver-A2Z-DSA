class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def segregate(self, head):
        dummyz, dummyo, dummyt = Node(-1), Node(-1), Node(-1)
        zero, ones, twos = dummyz, dummyo, dummyt
        while head:
            if head.data == 0:
                zero.next = Node(0)
                zero = zero.next
            elif head.data == 1:
                ones.next = Node(1)
                ones = ones.next
            else:
                twos.next = Node(2)
                twos = twos.next
            head = head.next
        ones.next = dummyt.next
        if dummyz.next:
            zero.next = dummyo.next
            return dummyz.next
        else:
            return dummyo.next
