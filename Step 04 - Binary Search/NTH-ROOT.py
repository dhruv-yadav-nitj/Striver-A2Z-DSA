import math


class Solution:
    def NthRoot(self, n, m):
        low, high, ans = 0, m, -1
        while low <= high:
            mid = (low + high) // 2
            res = math.pow(mid, n)
            if res == m:
                return mid
            elif res < m:
                low = mid + 1
            else:
                high = mid - 1
        return ans
