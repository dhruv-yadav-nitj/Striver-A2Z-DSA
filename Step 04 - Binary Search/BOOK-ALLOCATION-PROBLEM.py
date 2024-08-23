from typing import List


class Solution:
    def findPages(self, n: int, arr: List[int], m: int) -> int:
        if m > n:
            return -1

        def isValid(limit: int) -> int:
            count, curr = 1, 0
            for item in arr:
                if item > limit:
                    return int(1e9)
                if curr + item <= limit:
                    curr += item
                else:
                    count += 1
                    curr = item
            return count

        low, high = 0, sum(arr)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            students = isValid(mid)
            if students <= m:
                '''
                Why are we considering ans = mid in the case when students < m? ->
                1. Its bcz in this case also we need to reduce the upper_bound of our range to reduce the mid so that more
                students can be accommodated.
                2. Second reason to ye hain ki like if we have m = 5 and we have accommodated 3 students on the basis
                of our current mid, then we can do one thing ki 1st student ko mid jitna page de diaa jaae and baaki students
                ko thoda km km diaa jaae taaki saare usi mein accommodate ho jaae. Bcz we only want to consider the max
                page accommodated to any student to wo (mid ho jaaega) and baaki students ko mid se km mile tb saare
                accommodate ho jaaenge usi mein!
                '''
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
