from typing import List


class Solution:
    def maximumMeetings(self, n: int, start: List[int], end: List[int]) -> int:
        arr = []
        for i in range(n):
            arr.append((start[i], end[i]))
        last = count = 0
        arr.sort(key=lambda x: x[1])
        for s, e in arr:
            if s > last:
                count += 1
                last = e
        return count
