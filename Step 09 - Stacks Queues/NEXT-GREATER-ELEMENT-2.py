from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        n = len(nums)
        ans = [-1 for _ in range(n)]
        stack = []
        for i in range(n - 1, -1, -1):
            while len(stack) and stack[-1] <= nums[i]:
                stack.pop()
            if len(stack):
                ans[i] = stack[-1]
            else:
                ans[i] = -1
            stack.append(nums[i])
        return ans[:n // 2]
