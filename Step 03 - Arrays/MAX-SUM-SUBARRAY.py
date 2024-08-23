from typing import List
from sys import maxsize
# KADANE'S ALGORITHM


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, temp = -maxsize - 1, 0
        for item in nums:
            temp += item
            ans = max(ans, temp)
            if temp < 0:
                temp = 0
        return ans
