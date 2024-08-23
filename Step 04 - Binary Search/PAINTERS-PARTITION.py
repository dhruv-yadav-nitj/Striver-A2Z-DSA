from typing import List


class Solution:
    def minTime(self, arr: List[int], n: int, k: int):
        def isValid(time: int):
            count, curr = 1, 0
            for item in arr:
                if item > time:
                    return False
                if curr + item <= time:
                    curr += item
                else:
                    count += 1
                    curr = item
            return count <= k
        low, high, ans = 0, sum(arr), 0
        while low <= high:
            mid = (low+high)//2
            if isValid(mid):
                ans, high = mid, mid-1
            else:
                low = mid + 1
        return ans
