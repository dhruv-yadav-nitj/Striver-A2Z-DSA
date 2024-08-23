from typing import List
from sys import maxsize


# METHOD 1 : BRUTE FORCE
class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -maxsize
        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod *= nums[j]
                ans = max(ans, prod)
        return ans


# BETTER APPROACH
class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        pref = suff = 1
        ans, n = -maxsize, len(nums)
        for i in range(n):
            pref *= nums[i]
            suff *= nums[n-1-i]
            ans = max(ans, pref, suff)
            if not pref:
                pref = 1
            if not suff:
                suff = 1
        return ans
