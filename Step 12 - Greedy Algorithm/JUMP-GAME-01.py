from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        flag, j = False, None
        for i in range(n - 2, -1, -1):
            if not flag and nums[i] == 0:
                flag = True
                j = i
            if flag and nums[i] > j - i:
                flag = False
        return not flag
