from typing import List
from collections import Counter, defaultdict
import heapq


# Using purely Hashtable (Better)
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = [(key, value) for key, value in Counter(nums).items()]
        nums.sort(reverse=True, key=lambda x: x[1])
        return [nums[i][0] for i in range(k)]


# Using Heap with Hashtable
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int, Counter(nums))
        arr = []
        for key, value in mp.items():
            arr.append((-value, key))
        heapq.heapify(arr)
        ans = []
        while k:
            _, item = heapq.heappop(arr)
            ans.append(item)
            k -= 1
        return ans
