class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None


class Solution:
    def findPairsWithGivenSum(self, target: int, head: Optional['Node']) -> List[List[int]]:
        tail = head
        while tail.next:
            tail = tail.next
        ans = []
        while head and tail and head.data < tail.data:
            temp = head.data + tail.data
            if temp == target:
                ans.append([head.data, tail.data])
                head = head.next
                tail = tail.prev
            elif temp < target:
                head = head.next
            else:
                tail = tail.prev
        return ans
