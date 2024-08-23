from typing import List
import heapq
from collections import deque


class Solution1:
    """
    Using Priority Queue
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pq = []
        for i in range(k):
            item = nums[i]
            heapq.heappush(pq, (-item, i))
        ans = [-pq[0][0]]
        for i in range(k, n):
            left = i - k
            item = nums[i]
            while len(pq) and pq[0][1] <= left:
                heapq.heappop(pq)
            heapq.heappush(pq, (-item, i))
            ans.append(-pq[0][0])
        return ans


class Solution2:
    """
    Using Deque
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        n = len(nums)
        for i, item in enumerate(nums):
            while len(dq) and dq[0] <= i - k:
                dq.popleft()
            while len(dq) and nums[dq[-1]] <= item:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                ans.append(nums[dq[0]])
        return ans
