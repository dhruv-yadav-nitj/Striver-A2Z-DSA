from typing import List

mod = int(1e9 + 7)


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        next_smaller = [n for _ in range(n)]
        stack = []
        for i in range(n - 1, -1, -1):
            while len(stack) and arr[stack[-1]] >= arr[i]:  # edge case fix! -> arr: [1, 1] (duplicates)
                stack.pop()
            if len(stack):
                next_smaller[i] = stack[-1]
            stack.append(i)

        prev_smaller = [-1 for _ in range(n)]
        stack = []
        for i in range(n):
            while len(stack) and arr[stack[-1]] > arr[i]:
                stack.pop()
            if len(stack):
                prev_smaller[i] = stack[-1]
            stack.append(i)

        ans = 0
        for i in range(n):
            contri = (i - prev_smaller[i]) * (next_smaller[i] - i)
            ans += contri * arr[i]
        return ans % mod
