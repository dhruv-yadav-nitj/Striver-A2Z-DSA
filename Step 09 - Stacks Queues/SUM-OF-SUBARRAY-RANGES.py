from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        maxi = self.subarrayMaximum(nums)
        mini = self.subarrayMinimum(nums)
        return maxi - mini

    def subarrayMinimum(self, nums: List[int]):
        n = len(nums)
        prev_smaller = [-1 for _ in range(n)]
        stack = []
        for i in range(n):
            while len(stack) and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if len(stack):
                prev_smaller[i] = stack[-1]
            stack.append(i)
        next_smaller = [n for _ in range(n)]
        stack = []
        for i in range(n - 1, -1, -1):
            while len(stack) and nums[stack[-1]] > nums[i]:
                stack.pop()
            if len(stack):
                next_smaller[i] = stack[-1]
            stack.append(i)
        return sum([nums[i] * (i - prev_smaller[i]) * (next_smaller[i] - i) for i in range(n)])

    def subarrayMaximum(self, nums: List[int]):
        n = len(nums)
        prev_greater = [-1 for _ in range(n)]
        stack = []
        for i in range(n):
            while len(stack) and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if len(stack):
                prev_greater[i] = stack[-1]
            stack.append(i)
        next_greater = [n for _ in range(n)]
        stack = []
        for i in range(n - 1, -1, -1):
            while len(stack) and nums[stack[-1]] < nums[i]:
                stack.pop()
            if len(stack):
                next_greater[i] = stack[-1]
            stack.append(i)
        return sum([nums[i] * (i - prev_greater[i]) * (next_greater[i] - i) for i in range(n)])
