from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        # first sort for intervals[i][0] and if equal then sort wrt intervals[i][1]
        ans, n = [], len(intervals)
        start, end = intervals[0][0], intervals[0][1]
        if n <= 1:  # Edge Case: [[]] or [[1, 4]]
            return intervals
        for i in range(1, n):
            s, e = intervals[i]
            if s <= end:
                end = max(end, e)  # Edge Case: [[1, 4], [2, 3]]
            else:
                ans.append([start, end])
                start, end = s, e
            if i == n-1:
                ans.append([start, end])
        return ans
