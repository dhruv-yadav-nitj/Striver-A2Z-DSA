class Solution:
    # Max Heap
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def buildHeap(self, arr, n):
        pass

    def HeapSort(self, arr, n):
        for i in range(n // 2, -1, -1):
            self.heapify(arr, n, i)
        size = n
        while size > 0:
            arr[0], arr[size - 1] = arr[size - 1], arr[0]
            size -= 1
            self.heapify(arr, size, 0)
