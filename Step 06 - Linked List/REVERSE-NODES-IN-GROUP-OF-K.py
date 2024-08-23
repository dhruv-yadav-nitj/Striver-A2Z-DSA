from typing import Optional

'''
Important Given Constraints:
1 <= k <= n
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def getkthnode(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 1
        while count < k and head:
            head = head.next
            count += 1
        return head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev, temp, next = None, head, None
        while temp:
            kthNode = self.getkthnode(temp, k)
            if kthNode is None:
                prev.next = temp
                break
            else:
                next = kthNode.next
                kthNode.next = None
                new = self.reverseList(temp)
                if temp == head:
                    head = new
                else:
                    prev.next = new
                prev = temp
                temp = next
        return head
