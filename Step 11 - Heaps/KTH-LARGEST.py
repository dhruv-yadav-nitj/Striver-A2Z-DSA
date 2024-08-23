from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x: -x, nums))
        heapq.heapify(nums)
        ans = None
        while k > 0:
            ans = heapq.heappop(nums)
            k -= 1
        return ans
