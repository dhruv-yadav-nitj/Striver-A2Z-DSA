from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        n, curr = 0, head
        while curr:
            n += 1
            curr = curr.next
        odd = n % 2
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, head
        while curr != slow:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        if odd:
            slow = slow.next
        while head and slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True

