from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(grumpy)
        ans = 0
        for i in range(n):
            if not grumpy[i]:
                ans += customers[i]
                customers[i] = 0
        pref = maxi = 0
        pref_arr = [0]
        for i in range(n):
            pref += customers[i]
            pref_arr.append(pref)
            if i >= minutes-1:
                maxi = max(maxi, pref_arr[i+1] - pref_arr[i+1-minutes])
        return ans + maxi
