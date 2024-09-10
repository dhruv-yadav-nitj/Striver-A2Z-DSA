from typing import Optional
from math import gcd


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        curr = head
        while curr.next:
            fwd: ListNode = curr.next
            gcd_val = gcd(curr.val, fwd.val)
            temp = ListNode(gcd_val)
            curr.next = temp
            temp.next = fwd
            curr = fwd
        return head
