from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def length(self, head: Optional[ListNode]) -> int:
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        return cnt

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = self.length(head)
        ans = []
        each = n // k
        extra = n % k
        for i in range(k):
            count = each + 1 if i < extra else each
            # for initial extra splits we would keep one extra node in them
            tail = ListNode(-1)
            curr = tail
            while head and count:
                curr.next = ListNode(head.val)
                head = head.next
                count -= 1
                curr = curr.next
            ans.append(tail.next)

        return ans
