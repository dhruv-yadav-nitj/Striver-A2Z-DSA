from typing import List


class BruteForce:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        for i in range(n):
            max_left = max(height[:i+1])
            max_right = max(height[i:])
            ans += min(max_left, max_right) - height[i]
        return ans


class Optimised:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0 for _ in range(n)]
        max_right = [0 for _ in range(n)]
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])
        max_right[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])
        ans = 0
        for i in range(n):  # though we can skip 0th and (n-1)th index -> bcz they will never in any case store water!
            ans += min(max_left[i], max_right[i]) - height[i]
        return ans


# Incomplete
class Efficient:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = height[0]
        right = height[-1]
        ans = 0
        for i in range(1, n - 2):
            pass
        return ans
