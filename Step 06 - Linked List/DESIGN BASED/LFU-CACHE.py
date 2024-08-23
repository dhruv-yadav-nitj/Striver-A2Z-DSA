"""
If this problem comes in Interview then only God can save us!
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.cnt = 1
        self.next = None
        self.prev = None


class List:
    def __init__(self):
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addFront(self, node):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node
        self.size += 1

    def removeNode(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1


class LFUCache:
    def __init__(self, capacity: int):
        self.keyNode = {}
        self.freqListMap = {}
        self.maxSizeCache = capacity
        self.minFreq = 0
        self.curSize = 0

    def updateFreqListMap(self, node):
        del self.keyNode[node.key]
        self.freqListMap[node.cnt].removeNode(node)
        if node.cnt == self.minFreq and self.freqListMap[node.cnt].size == 0:
            self.minFreq += 1

        node.cnt += 1
        if node.cnt not in self.freqListMap:
            self.freqListMap[node.cnt] = List()
        self.freqListMap[node.cnt].addFront(node)
        self.keyNode[node.key] = node

    def get(self, key: int) -> int:
        if key in self.keyNode:
            node = self.keyNode[key]
            self.updateFreqListMap(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.maxSizeCache == 0:
            return

        if key in self.keyNode:
            node = self.keyNode[key]
            node.value = value
            self.updateFreqListMap(node)
        else:
            if self.curSize == self.maxSizeCache:
                list_to_remove = self.freqListMap[self.minFreq]
                del self.keyNode[list_to_remove.tail.prev.key]
                list_to_remove.removeNode(list_to_remove.tail.prev)
                self.curSize -= 1

            self.curSize += 1
            self.minFreq = 1
            new_node = Node(key, value)
            if self.minFreq not in self.freqListMap:
                self.freqListMap[self.minFreq] = List()
            self.freqListMap[self.minFreq].addFront(new_node)
            self.keyNode[key] = new_node

# Example usage:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
