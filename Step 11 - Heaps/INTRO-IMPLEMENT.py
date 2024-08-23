from typing import List


# MIN-HEAP
class Heap:
    def __init__(self, arr: List[int]):
        self.heap = arr
        self.heapify()

    def insert(self, val: int):
        self.heap.append(val)
        self.heapify()

    def helper(self, arr: List[int], index: int):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        n = len(arr)
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest != index:
            arr[smallest], arr[index] = arr[index], arr[smallest]
            self.helper(arr, smallest)

    def heapify(self):
        arr = self.heap
        n = len(arr)
        for i in range(n // 2, -1, -1):
            self.helper(arr, i)

    def print(self):
        print(self.heap)

    def pop(self):
        self.heap.pop(0)
        self.heapify()


nums = [21, 12, 31, 12, 10, 19]
heap = Heap(nums)

heap.print()
heap.insert(1)
heap.print()
heap.pop()
heap.pop()
heap.print()
