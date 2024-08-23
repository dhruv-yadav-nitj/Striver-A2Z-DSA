from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ind = 1
        odd, even = ListNode(-1), ListNode(-1)
        curr = head
        dummyOdd, dummyEven = odd, even
        while curr:
            if ind & 1:
                odd.next = ListNode(curr.val)
                odd = odd.next
            else:
                even.next = ListNode(curr.val)
                even = even.next
            ind += 1
            curr = curr.next
        odd.next = dummyEven.next
        return dummyOdd.next
