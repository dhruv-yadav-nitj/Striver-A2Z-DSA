class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def addNode(head, p, data):
    back, front = head, head.next
    while p > 0:
        back, front = front, front.next
        p -= 1
    node = Node(data)
    node.prev, node.next = back, front
    back.next = node
    if front:
        front.prev = node
