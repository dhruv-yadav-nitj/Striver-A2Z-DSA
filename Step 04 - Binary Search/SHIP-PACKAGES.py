from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValid(limit: int) -> bool:
            curr, count = 0, 1
            for item in weights:
                if curr + item <= limit:
                    curr += item
                else:
                    count += 1
                    curr = item
                    if count > days or item > limit:
                        return False
            return count <= days

        low, high = min(weights), sum(weights)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


'''
1. exact days taken -> since we want min capacity -> we would reduce high
2. less days taken -> since we want min capacity -> we would reduce high
3. more days taken -> increase the capacity -> increase low
'''
