from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans, n, i = [], len(intervals), 0
        while i < n:
            start, end = intervals[i][0], intervals[i][1]
            j = i + 1
            while j < n and intervals[j][0] <= end:
                end = max(end, intervals[j][1])
                j += 1
            ans += [[start, end]]
            i = j
        return ans
