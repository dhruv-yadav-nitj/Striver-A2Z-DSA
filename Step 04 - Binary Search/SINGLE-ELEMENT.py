from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if mid == 0 and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if mid == n - 1 and nums[mid] != nums[mid - 1]:
                return nums[mid]
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            if mid & 1:
                if nums[mid - 1] == nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if mid + 1 < n and nums[mid] == nums[mid + 1]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1