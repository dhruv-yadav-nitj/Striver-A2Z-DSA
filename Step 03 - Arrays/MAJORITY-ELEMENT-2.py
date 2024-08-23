from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans1, ans2, vote1, vote2, n = -1, -1, 0, 0, len(nums)
        for item in nums:
            if item == ans1:
                vote1 += 1
            elif item == ans2:
                vote2 += 1
            elif vote1 == 0:
                ans1, vote1 = item, 1
            elif vote2 == 0:
                ans2, vote2 = item, 1
            else:
                vote1 -= 1
                vote2 -= 1
        vote1 = vote2 = 0
        for item in nums:
            if item == ans1:
                vote1 += 1
            elif item == ans2:
                vote2 += 1
        return [x[0] for x in [[ans1, vote1], [ans2, vote2]] if x[1] > n // 3]
