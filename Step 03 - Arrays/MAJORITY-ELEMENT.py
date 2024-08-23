from typing import List
# assume that majority element always exist!

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, vote = nums[0], 1
        for item in nums[1:]:
            if item == ans:
                vote += 1
            else:
                vote -= 1
                if vote == 0:
                    ans, vote = item, 1
        return ans
