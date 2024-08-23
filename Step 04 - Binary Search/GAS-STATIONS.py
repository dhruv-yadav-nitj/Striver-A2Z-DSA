from typing import List
import math


class Solution:
    def findSmallestMaxDist(self, stations: List[int], K: int):
        stations.sort()

        def isValid(d: int):
            count = 0
            for i in range(1, len(stations)):
                dis = stations[i] - stations[i - 1]
                if dis <= d:
                    continue
                else:
                    count += math.ceil(dis / d) - 1
            return count <= K

        ans = low = 0
        high = max(stations[i] - stations[i - 1] for i in range(1, len(stations)))
        while high - low >= 1e-6:
            mid = (low + high) / 2
            if isValid(mid):
                ans = mid
                high = mid
            else:
                low = mid
        return ans
