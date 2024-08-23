from typing import List, Optional
from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = PriorityQueue()
        ans = curr = ListNode(-1)
        i = 0
        '''
        "i" is used to act as second comparator for PriorityQueue in case when node.val gets equal for two nodes. Since
        head (a pointer or object instance) cant be used to compare.
        '''
        for heads in lists:
            if heads:
                pq.put((heads.val, i, heads))
            i += 1
        while not pq.empty():
            val, _, node = pq.get()
            curr.next = ListNode(val)
            curr = curr.next
            if node.next:
                pq.put((node.next.val, i, node.next))
            i += 1
        return ans.next
