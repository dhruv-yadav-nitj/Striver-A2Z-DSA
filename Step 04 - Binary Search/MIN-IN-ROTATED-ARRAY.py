from typing import List
from sys import maxsize


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        ans = maxsize
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= nums[low]:
                ans = min(ans, nums[low])
                low = mid + 1
            else:
                ans = min(ans, nums[mid])
                high = mid - 1
        return ans
