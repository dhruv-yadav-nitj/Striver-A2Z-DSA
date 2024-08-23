from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        def helper(ind: int, temp: List[int]) -> None:
            ans.append(temp)
            for i in range(ind, n):
                if i > ind and nums[i] == nums[i - 1]:
                    continue
                # pick and not pick at index
                # helper(i + 1, temp)
                temp2 = temp.copy()
                temp2.append(nums[i])
                helper(i + 1, temp2)

        helper(0, [])
        return ans
