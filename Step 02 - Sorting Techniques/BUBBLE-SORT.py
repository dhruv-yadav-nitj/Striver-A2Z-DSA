# ITERATIVE
class Solution:
    # Function to sort the array using bubble sort algorithm.
    def bubbleSort(self, arr, n):
        flag = True  # flag introduces to counter the case when there's no swapping -> then the array is sorted
        for i in range(n - 1, -1, -1):
            if flag:
                flag = False
                for j in range(i):
                    if arr[j] > arr[j + 1]:
                        flag = True
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


# RECURSIVE
class Solution:
    def bubbleSort(self, arr, n):
        if n > 1:
            for j in range(n-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            self.bubbleSort(arr, n-1)