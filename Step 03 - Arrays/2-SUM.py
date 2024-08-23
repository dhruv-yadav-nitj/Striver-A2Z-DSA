from typing import List


# USING SORTING AND TWO POINTERS
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(list(enumerate(nums)), key=lambda x: x[1])
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            if nums[i][1] + nums[j][1] == target:
                return [nums[i][0], nums[j][0]]
            elif nums[i][1] + nums[j][1] < target:
                i += 1
            else:
                j -= 1
        return []
