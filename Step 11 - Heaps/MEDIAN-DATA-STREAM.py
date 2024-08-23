import heapq

'''
Hint: We do not need whole array but only that two element which make up the median. Divide & Conquer!
Problem is not hard, but is having a lot edge cases!
nums: [5, 15, 1, 3] -> [5, 10, 5, 4] : median
'''

class MedianFinder:
    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if not (len(self.maxheap) + len(self.minheap)):
            heapq.heappush(self.maxheap, -num)
        elif len(self.maxheap) == len(self.minheap):
            if num < self.minheap[0]:
                heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
                heapq.heappush(self.minheap, num)
        else:
            if len(self.minheap) == 0:
                if num > -self.maxheap[0]:
                    heapq.heappush(self.minheap, num)
                else:
                    heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
                    heapq.heappush(self.maxheap, -num)
            elif num >= self.minheap[0]:
                heapq.heappush(self.minheap, num)
            else:
                if num < -self.maxheap[0]:
                    heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
                    heapq.heappush(self.maxheap, -num)
                else:
                    heapq.heappush(self.minheap, num)

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
