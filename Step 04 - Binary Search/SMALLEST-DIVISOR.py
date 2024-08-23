from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        if threshold < n:
            return -1

        def isValid(divisor: int):
            res = 0
            for item in nums:
                res += (item + divisor - 1) // divisor
                if res > threshold:
                    return False
            return res <= threshold

        low, high = 1, max(nums)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
