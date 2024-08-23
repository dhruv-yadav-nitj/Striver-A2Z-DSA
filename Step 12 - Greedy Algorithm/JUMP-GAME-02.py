from typing import List


# Dynamic Programming Approach -> T.C O(n^2)
class Solution1:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n)]

        def memo(index: int) -> int:
            if index == n - 1:
                return 0
            if nums[index] == 0:
                return int(1e9)
            if dp[index] != -1:
                return dp[index]
            ans = int(1e9)
            for i in range(1, nums[index] + 1):
                if index + i < n:
                    jump = 1 + memo(index + i)
                    ans = min(ans, jump)
            dp[index] = ans
            return ans

        return memo(0)


# LINEAR SOLUTION
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        count = i = j = max_reach = 0
        while i < n-1:
            max_reach = max(max_reach, i + nums[i])
            if i == j:
                count += 1
                j = max_reach
                if j >= n-1:
                    return count
            i += 1
        return -1
