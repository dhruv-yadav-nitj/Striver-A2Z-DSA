from typing import List
# NOTE: Given that nums[i] != nums[i+1] for all 'i' means there are no duplicates involved
# well this given criteria is necessary as well -> bcz then only this solution would work


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n - 1
        low, high = 1, n - 2
        while low <= high:
            mid = (low + high) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid - 1] > nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
