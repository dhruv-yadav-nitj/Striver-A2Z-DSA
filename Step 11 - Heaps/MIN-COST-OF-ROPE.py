from typing import List
import heapq

'''
Hint: Min Cost when we merge two smallest ropes!
'''

class Solution:
    def minCost(self, arr: List[int], n: int):
        heapq.heapify(arr)
        cost = 0
        while len(arr) > 1:
            a = heapq.heappop(arr)
            b = heapq.heappop(arr)
            cost += a + b
            heapq.heappush(arr, a+b)
        return cost

