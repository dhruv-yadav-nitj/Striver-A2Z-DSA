import math


class Solution1:
    def floorSqrt(self, x):
        return math.floor(math.sqrt(x))


class Solution:
    def floorSqrt(self, x):
        low, high, ans = 1, x, -1
        while low <= high:
            mid = (low + high) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
