from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        # method 1 : due to some reason not working on leetcode
        # nums = nums[::-1]
        # nums[:k] = nums[:k][::-1]
        # nums[k:] = nums[k:][::-1]
        # print(nums)

        # method 2 :
        nums[:] = nums[n - k:] + nums[:n - k]
