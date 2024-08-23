class Solution:
    def helper(self, arr, low, high):
        pivot, i, j = arr[low], low, high
        while i < j:
            while i < high and arr[i] <= pivot:
                i += 1
            while j > low and arr[j] >= pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quickSort(self, arr, low, high):
        if low < high:
            pivot = self.helper(arr, low, high)
            self.quickSort(arr, low, pivot - 1)
            self.quickSort(arr, pivot + 1, high)
