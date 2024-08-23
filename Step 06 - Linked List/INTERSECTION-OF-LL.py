from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getlength(self, head: Optional[ListNode]) -> int:
        curr = 0
        while head:
            curr += 1
            head = head.next
        return curr

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len1, len2 = self.getlength(headA), self.getlength(headB)
        if len1 > len2:
            return self.getIntersectionNode(headB, headA)
        k = len2 - len1
        slow, fast = headA, headB
        while k > 0:
            k -= 1
            fast = fast.next
        while slow and fast and slow != fast:
            slow = slow.next
            fast = fast.next
        if slow and fast and slow == fast:
            return slow
        else:
            return None
