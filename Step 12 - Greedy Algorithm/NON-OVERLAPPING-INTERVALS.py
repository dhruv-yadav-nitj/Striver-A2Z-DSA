from typing import List

'''
Explanation: https://www.youtube.com/watch?v=nONCGxWoUfM
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        i = 0
        n = len(intervals)
        ans = 0
        j = 1
        while i < n - 1 and j < n:
            s1, e1 = intervals[i]
            s2, e2 = intervals[j]
            if s2 < e1:
                ans += 1
                if e2 <= e1:
                    i = j
            else:
                i = j
            j += 1
        return ans
