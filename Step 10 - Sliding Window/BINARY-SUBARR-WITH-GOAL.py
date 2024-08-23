from typing import List
from collections import defaultdict


# USING TECHNIQUE USED IN PROBLEM 'Count number of sub-arrays with given sum'
class Solution1:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = pref = 0
        mp = defaultdict(int)
        mp[0] += 1
        for item in nums:
            pref += item
            x = pref - goal
            ans += mp[x]
            mp[pref] += 1
        return ans


# USING SLIDING WINDOW
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(target):
            ans = temp = i = j = 0
            n = len(nums)
            while j < n:
                temp += nums[j]
                while i <= j and temp > target:
                    temp -= nums[i]
                    i += 1
                ans += (j - i + 1)
                j += 1
            return ans
        return helper(goal) - helper(goal-1)
