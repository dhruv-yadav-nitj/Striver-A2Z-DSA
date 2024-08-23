from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def isValid(mid):
            count = temp = 0
            for item in bloomDay:
                if item <= mid:
                    temp += 1
                    if temp == k:
                        temp, count = 0, count + 1
                else:
                    temp = 0
            return count >= m

        low, high = min(bloomDay), max(bloomDay)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            print(low, mid, high)
            if isValid(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
