from collections import defaultdict


class MyStack:
    class StackNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.prev = defaultdict()
        self.tail = self.StackNode(-1)

    def push(self, data) -> None:
        node = self.StackNode(data)
        self.prev[node] = self.tail
        self.tail.next = node
        self.tail = self.tail.next

    def pop(self) -> int:
        ans = self.tail.data
        self.tail.next = None
        if self.tail in self.prev:
            self.tail = self.prev[self.tail]
        return ans


'''
Note: Queue can also be implemented using Linkedlist in the similar fashion only difference is in that case we have to
maintain two pointers one head and one tail for FIFO operation!
'''