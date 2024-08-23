from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(k):
            count = 0
            for item in piles:
                count += (item + k - 1)//k
                if count > h:
                    return False
            return count <= h

        low, high = 0, sum(piles)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if mid > 0 and isValid(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
