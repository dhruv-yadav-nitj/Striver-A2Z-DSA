from typing import List
import heapq
from queue import PriorityQueue

'''
heapq and PriorityQueue both are methods that can be used to implement Heaps in Python.
heapq have functions like heapq.heapify(_iterable), heapq.heappop(_iterable), heapq.heappush(_iterable)
PriorityQueue has functions like .put(_item), .get()
NOTE: Both implement min-heap!   
'''


class Solution:
    def mergeKArrays(self, arr: List[List[int]], k: int):
        pq = PriorityQueue()
        for i in range(k):
            pq.put((arr[i][0], i, 0))
        ans = []
        while not pq.empty():
            item, row, col = pq.get()
            ans.append(item)
            if col+1 < k:
                pq.put((arr[row][col+1], row, col+1))
        return ans
