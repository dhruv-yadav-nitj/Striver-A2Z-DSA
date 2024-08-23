from typing import Optional, Tuple

# SIMILAR TO ROTATE ARRAY
'''
Here we have applied the technique which we applied in Rotating Array.
1. Reverse the whole array
2. Reverse the first k elements
3. Reverse the next n-k elements
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def reverse(self, head: Optional[ListNode], k: int) -> Tuple:
        prev, curr = None, head
        while curr and k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            k -= 1
        return prev, curr

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = self.getLength(head)
        if n <= 1:
            return head
        k = k % n
        if k == 0:
            return head
        head, _ = self.reverse(head, n)
        head, temp = self.reverse(head, k)
        curr = head
        while curr.next:
            curr = curr.next
        t, _ = self.reverse(temp, n - k)
        curr.next = t
        return head
