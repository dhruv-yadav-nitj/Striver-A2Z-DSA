from typing import List


# THIS PROBLEM IS SAME AS BOOK ALLOCATION PROBLEM!


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isValid(limit: int) -> bool:
            curr, count = 0, 1
            for item in nums:
                if item > limit:
                    return False
                if curr + item <= limit:
                    curr += item
                else:
                    count += 1
                    curr = item
            return count <= k

        low, high = min(nums), sum(nums)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
