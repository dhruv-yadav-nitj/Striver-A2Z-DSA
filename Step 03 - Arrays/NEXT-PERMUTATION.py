from typing import List
from sys import maxsize


# GENERATING ALL POSSIBLE PERMUTATIONS
class Solution1:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n, ans = len(nums), []

        def recursion(arr: List[int], index: int):
            if index == n:
                ans.append(arr[:])
                return
            for i in range(index, n):
                arr[i], arr[index] = arr[index], arr[i]
                recursion(arr, index + 1)
                arr[i], arr[index] = arr[index], arr[i]

        recursion(nums, 0)
        print(ans)


arr = [1, 2, 3]
obj = Solution1()
obj.nextPermutation(arr)


# OPTIMISED SOLUTION
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            nums.sort()
        else:
            k = i + 1
            for j in range(i+2, n):
                if nums[i] < nums[j] <= nums[k]:
                    k = j
            nums[i], nums[k] = nums[k], nums[i]
            nums[i+1:] = reversed(nums[i+1:])

