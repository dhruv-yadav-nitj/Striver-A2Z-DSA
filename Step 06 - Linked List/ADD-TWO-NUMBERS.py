from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            curr = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            head.next = ListNode(curr % 10)
            carry = curr // 10
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
