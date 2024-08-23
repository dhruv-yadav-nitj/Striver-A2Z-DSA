from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def helper(ind: int, curr: List[int]):
            if ind == n:
                ans.append(curr)
                return
            # not-pick
            helper(ind + 1, curr)
            # pick
            temp = curr.copy()
            temp.append(nums[ind])
            helper(ind+1, temp)  # method 1
            # helper(ind + 1, curr+[nums[ind]]) -> method2

        helper(0, [])
        return ans
