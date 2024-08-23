from typing import List

'''
Similar to 'Merge Intervals' Problem
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        n = len(intervals)
        i = 0
        ans = []
        while i < n:
            start, end = intervals[i][0], intervals[i][1]
            j = i + 1
            while j < n and intervals[j][0] <= end:
                end = max(end, intervals[j][1])
                j += 1
            ans.append([start, end])
            i = j
        return ans
