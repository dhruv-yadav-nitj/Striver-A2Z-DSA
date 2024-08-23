from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = j = 0
        n = len(nums)
        while j < n:
            while j < n and nums[j] == 0:
                j += 1
            nums[i] = nums[j]
            i += 1
            j += 1
        if i < n:
            nums[i:] = [0] * (n - i)
