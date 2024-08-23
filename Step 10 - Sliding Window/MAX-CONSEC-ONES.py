from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = i = j = ans = 0
        n = len(nums)
        while j < n:
            if nums[j] == 0:
                count += 1
            if count > k:
                ans = max(ans, j - i)
                while i <= j and count > k:
                    if nums[i] == 0:
                        count -= 1
                    i += 1
            j += 1
        ans = max(ans, j - i)
        return ans
