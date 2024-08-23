from typing import List


class Solution:
    def solve(self, n: int, k: int, stalls: List[int]):
        if n < k:
            return -1
        stalls.sort()

        def isValid(mid: int):
            count, last = 1, stalls[0]
            for item in stalls[1:]:
                if item - last >= mid:
                    count += 1
                    last = item
            return count >= k

        low, high = 0, stalls[-1] - stalls[0]
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
